"""
General results:
    * Process Pool Executor works GREAT for intensive CPU tasks
    * Elapsed times:
        for loop calling a function: 36.7
        List comprehension calling a function: 38.9
        list map calling a function: 36.3
        Process Pool Executor calling a function: 19.5
        Thread Pool Executor calling a function: 38.9
"""

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from time import monotonic, process_time
from math import floor, sqrt

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    115797848077099,
    1099726899285419,
]


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(floor(sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


elapsed = monotonic()
result = []
for prime in PRIMES:
    result.append(is_prime(prime))
print(f"for loop calling a function: {monotonic() - elapsed}")

elapsed = monotonic()
result = [is_prime(prime) for prime in PRIMES]
print(f"List comprehension calling a function: {monotonic() - elapsed}")

elapsed = monotonic()
result = list(map(is_prime, PRIMES))
print(f"list map calling a function: {monotonic() - elapsed}")

elapsed = monotonic()
with ProcessPoolExecutor() as executor:
    result = []
    for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
        result.append(prime)
        print(f"{number} is prime: {prime}")
print(f"Process Pool Executor calling a function: {monotonic() - elapsed}")

elapsed = monotonic()
with ThreadPoolExecutor() as executor:
    future_if_prime = {executor.submit(is_prime, prime): prime for prime in PRIMES}
    result = []
    for future in as_completed(future_if_prime):
        number = future_if_prime[future]
        try:
            result.append(future.result())
        except Exception as exc:
            print(f"{number} generated an exception: {exc}")
        else:
            print(f"{number} is prime: {result[-1]}")
print(f"Thread Pool Executor calling a function: {monotonic() - elapsed}")

print()
