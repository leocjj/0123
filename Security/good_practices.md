## Documentation
Key things to consider:
- document your code interfaces and API contracts
- define your documentation strategy:
    - what is your overall documentation strategy? 
    - what do you put in the README.md file of the project?
    - do you need to update a wider documentation?
    - what tool do you use for diagrams? 
    - do you use [lightweight architecture decision records](https://adr.github.io/)?
    - do you store the documentation along with the project in Git? or maybe use a separate tool?
    - if you store it within the project, what is the recommended folder structure?

## General (micro)services design guidelines
Key things to consider:
- use a blueprint/template/archetype as a starting point for all your (micro)services
- have the blueprint already bundled with all the common libraries, plugins, etc. and aligned to the standards
- each (micro)service must start with one command
- (micro)services will process data only through APIs/events; there is no back-door
- (micro)services are self-contained
- all (micro)services are [12 factor apps](https://12factor.net/) and [even more](https://tanzu.vmware.com/content/blog/beyond-the-twelve-factor-app)

## Code formatting/styling
Just choose one and apply it consistently. Auto-format before commit if possible.

## Naming conventions
Just choose one and apply it consistently.

## API standards
Key things to consider:
- follow REST naming practices (nouns, plurals, the usual stuff) - pick one, [the internet is full of guidelines](https://www.google.com/search?q=rest+naming+best+practices&oq=rest+naming+practices), **but be consistent**
- be consistent with the naming; this applies for everything, not only the endpoints: payload object naming, properties etc. camelCase, snake_case, kebab-case/hyphen-case etc. Again, just choose something, **but be consistent**
- make `POST, PUT, PATCH` return bodies with meaningful responses
- use meaningful [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes), rather than `400` for everything that goes wrong
- **all** endpoints must return meaningful error cases
- use an error catalogue (more details in the Error Handling section)
- consider something like [OpenAPI](https://www.openapis.org/) and consider also doing contract-first development i.e., write the OpenAPI contract initially, socialize it with your (internal) consumers; this also enables better parallel development
- document your OpenAPI contracts with meaningful descriptions and examples
- **all** (internal) APIs must use CorrelationId/TraceId headers
- **all** API inputs must be very restrictive by default
- **all** APIs (internal or external) must be authenticated and ideally also with authorization in place
- **all** APIs must re-use the same common data structures; either generic ones like Address, Person, Country, etc, but also define business specific ones
- **all** APIs (internal or external) are exposed over **HTTPS** only
- for the relevant APIs consider returning security headers within the response like: `Cache-Control: no-store, Content-Security-Policy: frame-ancestors 'none', Content-Type, Strict-Transport-Security, X-Content-Type-Options: nosniff, X-Frame-Options: DENY` 
- internal APIs do not communicate to each others via the internet (unless this is something deliberate or required by the architecture)
- do not expose management endpoints over the internet; if this is something required, use authentication
- make sure **all** APIs are enforcing strict validation for the received requests: do not allow undocumented JSON fields, reject malformed JSONs, etc
- make proper use of data types; don't have everything as a String
- use enumerated values whenever possible
- add length restrictions for strings and min/max for numbers
- add patterns restricting input for each string
- for some properties it's easier to find patterns as they have clear definitions; a country code will always follow the `[A-Z]+`; for others, it's a bit more difficult; a `lastName` property needs to be quite loose, considering all names in all languages;
  the recommendation is at least to prevent strange characters like the Unicode control chars, separators or symbol; a recommended pattern object is the following: `^[^\p{C}\p{Z}\p{So}]*[^\p{C}\p{so}]+[^\p{C}\p{Z}\p{So}]*$`; this doesn't mean that you are now
  protected from any type of injection; you still need to have a good understanding where the data goes and how it is processed, but at least you won't get [an emoji breaking your system](https://www.vice.com/en/article/gv5jgy/iphone-emoji-break-apps)
  

## Logging standards
Key things to consider:
- logging format: comma separated `key=value` pairs? json objects? choose something which is friendly to your tooling
- always include the `CorrelationId/TraceId` in each log line; this will make it easier for tools to create dashboards
- include information in logs that will make it easier to understand what's happening: for which entity? business area? is it success? failure?
- some [good practices](https://www.javacodegeeks.com/2011/01/10-tips-proper-application-logging.html)
- use an abstraction over the actual logging implementation; for example in Java: [slf4j](http://www.slf4j.org/) with [logback](http://logback.qos.ch/) as implementation
- treat logging as a cross-cutting-concern; leverage [Aspects](https://en.wikipedia.org/wiki/Aspect-oriented_programming); log within methods only exceptionally; this will limit people from logging sensitive stuff
- don't treat logging like `let's log everything and see if we needed it afterwards` and dump full requests/responses; be deliberate in what you log, even when logging with `debug` or lower levels
- more on [Logging Data]()

## Data standards
Key things to consider:
- use existing ISO standards for widely known objects: [Currencies](https://en.wikipedia.org/wiki/ISO_4217), [Dates](https://en.wikipedia.org/wiki/ISO_8601), [Amounts](https://en.wikipedia.org/wiki/ISO_4217) just to name a few
- define business specific objects to be re-used
- apply these standards for API objects, database entities and events

### Processing Data
Key things toc consider:
- sanitize data before processing it; this is a good sanitization regex `^[^\p{C}\p{Z}\p{So}]*[^\p{C}\p{so}]+[^\p{C}\p{Z}\p{So}]*$`; it won't prevent all problems, but it will strip weird chars that [can cause your system to crash](https://www.instana.com/blog/how-a-slack-zero-width-space-character-broke-a-kubernetes-deployment/)
- make sure that you don't transmit data from input towards internal elevated access operations like database queries, command line execution etc.; use parametrized queries for DB, be very specific around what you get and what you pass forward
- favor whitelisting instead of blacklisting when you need to make decisions or when plan to restrict processing for specific input
- overall favor [defensive programming practices](https://en.wikipedia.org/wiki/Defensive_programming)
- make sure you use efficient XML parsers that are not vulnerable to [XXE](https://owasp.org/www-community/vulnerabilities/XML_External_Entity_%28XXE%29_Processing) or similar attacks; ideally do not accept XML as input unless forced by the context

### Logging Data
Key things to consider:
- don't log sensitive data; if you still need it for some reason, mask/obfuscate the data; what `sensitive` means depends on your business and regulations
- create/use a library that **masks by default** the most sensitive data within your platform; for example if you're processing payments, card numbers must be masked by default; **you shouldn't leave this decision to each individual**
- consider extending the library each time new sensitive data is added; you must also balance performance when adding too much data
- the logging library must also allow specific configuration so that each individual service can mask additional data without extending the library
- the logging library must provide on-demand sanitization (i.e., by calling specific methods); this will make sure the same sanitization techniques are applied for all cases
- the logging library must sanitize data before logging it (for example by removing all the characters matching `\p{Z}\p{C}\p{So}`)
- the logging library must also remove CR and LF characters in order to prevent [CRLF injection](https://owasp.org/www-community/vulnerabilities/CRLF_Injection)
- have a clear log archiving strategy

### Storing Data
Key things to consider:
- data must not be store `in case you need it`; you must only store data that is relevant in current context or foreseeable future
- storing data introduces compliance obligations; make sure you are aware of those
- some data cannot be stored in clear (one example is credit card numbers); use hardware or software [HSM](https://en.wikipedia.org/wiki/Hardware_security_module) for encryption
- don't store secrets (passwords, encryption keys, ssh keys, private keys) in version control on plain text files; use dedicated products or services for this like Vaults, HSMs
- use [salt](https://en.wikipedia.org/wiki/Salt_(cryptography)) and/or [pepper](https://en.wikipedia.org/wiki/Pepper_(cryptography)) when encrypting or hashing sensitive data; this will prevent brute-force attacks
- consider building (or using) a centralized service that will [tokenize sensitive data](https://en.wikipedia.org/wiki/Tokenization_(data_security))
- you should tokenize any data that is under some sort of regulation: card data, PII data, etc.; use tokens instead of the actual data in all (micro)services and detokenize only when needed; this will minimize the compliance footprint and will also give better control around the data
- enhance the security of the tokenization solution; do not allow external access to its APIs

## Events/messaging standards
Key things to consider:
- create an event catalogue so that everyone is aware of the purpose of each event
- use event schemas for validation
- avoid using generic events where you dump everything; you might leak sensitive information without wanting it
- consider exchanging Tokens instead of the actual data for sensitive information
  
## Configuration handling
Key things to consider:
- avoid hardcoding configuration in source files
- consider using [centralized configuration management](https://docs.microsoft.com/en-us/dotnet/architecture/cloud-native/centralized-configuration)
- segregate configuration by environment
- **do not store secrets (passwords, api keys, ssh keys, private keys, etc) in source files or in version control**; use proper [Secrets Vault systems](https://www.vaultproject.io/)
- **do not leave default credentials** for any deployable unit (either cloud service, off the shelf products, or your own (micro)services)
- do not put test-only code or configuration in production
- don't build `test only` backdoors inside your (micro)service
- use version control to track configuration changes
- have mechanisms in place for configuration integrity checking


## Error handling 
Key things to consider:
- consider treating exception and errors as a cross-cutting concern; leverage [Aspects](https://en.wikipedia.org/wiki/Aspect-oriented_programming), use something like [ControllerAdvices](https://www.baeldung.com/exception-handling-for-rest-with-spring) or similar
- consider embedding the logic for the most common exceptions/errors (validation issues, resource not found, malformed messages) into a shared library; this will make the interaction between (micro)services predictable and with less friction
- use an error catalogue
- use error codes (e.g. `MICRO-4221` - bad request due to structural validation, `MICRO-4222` - bad request due to business validation)
- do not leak internal state in responses; avoid passing `e.getMessage()`; each error returned must be deliberately created from the root cause, but without leaking internal data
- use a catch-all mechanism in order to avoid leaking internal state for unexpected exceptions; you can just catch `Exception` in the global error handler and return a `500`
- return the same object for all errors to enable a consistent experience
- document all error cases in your API documentation with the appropriate HTTP Status code; if you use OpenAPI, document all possible HTTP status codes, even if they return the same OpenAPI object

## Branching strategy and commits
Key things to consider:
- use a [simple branching strategy](https://martinfowler.com/articles/branching-patterns.html#LookingAtSomeBranchingPolicies); trunk-based, github-flow, etc.; just pick one
- use meaningful names for your repos and branches
- use [descriptive commits](https://chris.beams.io/posts/git-commit/); it will make it easier to trace changes in the future
- use small commits to better isolate changes
- use smart commits i.e., provide a link to the task from the task management system
- consider using pre-commit hooks to validate the commits
- **do not include sensitive information in commit messages**
- **pay attention when enabling remote access to your repos; especially when repos are hosted in cloud**

## Code review
Key things to consider:
- do code reviews (be kind, assertive, specific, [all the good stuff](https://mtlynch.io/code-review-love/))
- let the boring stuff to the tools and focus on the functional aspects and alignment to standards and practices
- if you find the same issue repeated over and over, add it within the standards
- consider using checklists, at least initially until people make it a habit on focusing on the same stuff

## Tooling and 3rd party libraries
Key things to consider:
- have a process in place for introducing new tooling; do a trade-off analysis and present it in a wider group to get acceptance/agreement and make sure you address wider cases
- when selecting open source software pay attention to [the license(s)](https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licences)
- create a list with licenses that can be used without asking, licenses that needs to be discussed and licenses which are not allowed to be used
- don't take the first (or latest) shiny tool/library/product you find; consider things like: is it stable?, is it maintained? does it have a track record? 
- consider using tools such as [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/), [License Plugin](https://www.mojohaus.org/license-maven-plugin/) or even more complex tools such as [Black Duck](https://www.blackducksoftware.com/)
- create a list with the agreed tooling/libraries where people can choose from
- update your dependencies frequently

## Code Analysis
Key things to consider:
- use one or multiple tools to analyze your code
- you must have (at least) one tool focused on the general coding practices and (at least) one focused on security practices
- some good tools for general code analysis (Java): [Sonarqube](https://www.sonarqube.org/), [PMD](https://pmd.github.io/), [SpotBugs](https://spotbugs.github.io/)
- some good tools for security code analysis: [Veracode](https://www.veracode.com/), [Checkmarx](https://www.checkmarx.com/), [Sonarqube](https://www.sonarqube.org/)
- you don't need to agree with all the practices that are part of the standard rule sets of these tools (although usually they are aligned with industry recommendations); you can create a subset of rules tailored to your context

## Testing
Key things to consider:
- automate testing at all levels: unit, integration, component, API, end-to-end, etc.
- focus on negative and boundary testing, not only on happy scenarios; [CATS](https://github.com/Endava/cats) is a good option for API testing
- don't ignore failing tests, even those failing intermittently; they might hide a serious underlying issues
- tests must be resilient and self-sufficient
- tests must use a similar and predictable approach
- tests must not depend on complicated external setup; they must either be self-sufficient by mocking dependencies, using in-memory setups or [testcontainers](https://www.testcontainers.org/) or just depend on the (micro)service being deployed; any other steps will just complicate the setup and introduce complexity
- consider adding some [security testing inside the pipeline](https://www.zaproxy.org/)
- consider [mutation testing](https://en.wikipedia.org/wiki/Mutation_testing)

## CI/CD
Key things to consider:
- include [Quality Gates](https://martinfowler.com/articles/is-quality-worth-cost.html#HighQualitySoftwareIsCheaperToProduce) for the most important stuff; they must act as checkpoints and fail the build if they are not met
- Quality Gates must be inline with these standards and automate the process of checking that each (micro)service is aligned
- a sample CI/CD pipeline might look like this:
    - compile and build
    - check formatting
    - run tests and check coverage
    - run mutation testing
    - run code analysis
    - run secure code analysis
    - check 3rd party libraries for vulnerabilities
    - check 3rd party library licenses
    - deploy
    - run API tests
    - run other types of testing
- this might seem too much (or lengthy), but for a microservice this is quite fast
- script your pipeline
- don't couple the pipeline to the (micro)services
- use a template pipeline for all (micro)services

## Authentication and Authorisation
Key things to consider:
- don't roll your own authentication and authorisation; use standards products and services
- authenticate all your APIs, internal and external; [just pick something proven](https://dzone.com/articles/four-most-used-rest-api-authentication-methods)
- use separate authentication and authorisation mechanism for external and internal calls i.e., use one set of credentials/mechanism to authenticate external calls and a separate one for internal calls
- credentials are always encrypted both in-flight and at-rest
- use HTTPS for all APIs, internal or external
- do not accept authentication credentials via HTTP GET; use only HTTP headers or HTTP POST/PUT
- **do not log credentials** not even when `debug` on; have your logging library also act as `catch all` for credentials
- make sure your authorisation and authentication mechanism allows granular control and management i.e., you can restrict number of calls per operation, revoke access, issue additional credentials, etc.
- consider using a centralized Identity Provider and common libraries
- use enhanced security controls for highly sensitive APIs/services ([mutual TLS](https://en.wikipedia.org/wiki/Mutual_authentication) for APIs, [MFA](https://en.wikipedia.org/wiki/Multi-factor_authentication) for access to services)
- use [nonces](https://support.kraken.com/hc/en-us/articles/360000906023-What-is-a-nonce-) to prevent replay attacks
- always design and build with the [least privilege principle](https://us-cert.cisa.gov/bsi/articles/knowledge/principles/least-privilege) in mind

## General Security Practices
Key things to consider:
- **don't ever roll your own encryption**; you cannot reinvent the wheel in this space
- use industry recommended algorithms: [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) 256; [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) 2048+, [SHA-2](https://en.wikipedia.org/wiki/SHA-2) 512.
- use TLS 1.3+ for transport security
- use [salt](https://en.wikipedia.org/wiki/Salt_(cryptography)) and/or [pepper](https://en.wikipedia.org/wiki/Pepper_(cryptography)) when encrypting or hashing sensitive data; this will prevent brute-force attacks
- check your programming language practices for dealing with sensitive information; for example in Java you must use `byte[]` rather than `String` to handle password, card numbers, social security numbers, etc.; you must minimize the time the data stays in memory and clear the objcts after use


## Quality attributes
As we've seen above, SDLC standards and practices are not always directly related to security. Same applies for quality attributes. 
Shortcomings in current design and approach can cause your application to go down, even if it is not caused by a  `true` security problem.

Key things to consider for `Performance`:
- use pooling for connection to expensive resources like DB, APIs, etc.
- use thread pools
- use caching
- use proper collections when manipulating data
- use parallel programming if applicable
- make sure you understand how your ORM generates queries
- avoid loading big resources in memory, use data streams
- baseline your performance per (micro)service instance so that you know when to scale
- do regular load and performance testing

Key things to consider for `Resilience`:
- use circuit breakers, retries, timeouts, rate-limiting
- have clear fallback strategies when dependent APIs are not available
- some great resources on the topic: [Resilient Systems Part 1](https://engineering.grab.com/designing-resilient-systems-part-1) and [Resilient System Part 2](https://engineering.grab.com/designing-resilient-systems-part-2)
- make all APIs [Idempotent](https://stripe.com/blog/idempotency)
- don't store state within one (micro)service instance; use a distributed cache for that

Key things to consider for `Availability and Scalability`:
- don't make your (micro)services design limit horizontal scaling
- plan for failure, have automated mechanisms in place for auto-scaling based on load
- consider sharding, read-only replicas
- use multi-region deployments

Key things to consider for `Observability and Monitoring`:
- all (micro)services must expose health endpoints covering both application and the underlying container
- the health endpoint must return information about all its dependencies: db, encryption service, APIs it connects to, event bus, etc.
- leverage the standardized logging to create meaningful operational dashboards

## Automate
Automate everything. Automation makes it predictable and consistent. 
The CI/CD pipeline should be the place where you automate all checks that will assess your (micro)service from a quality perspective.
Tools like [Semgrep](https://semgrep.dev/) can bring automation with less effort for standards not obviously suited for automation.
