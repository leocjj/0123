"""
General results:
    * Thread Pool Executor works GREAT for intensive IO tasks.
    * Process Pool Executor works GOOD for intensive IO tasks.
    * Elapsed times:
        Dict comprehension calling a function: 40.3
        Process Pool Executor calling a function: 12.6
        Thread Pool Executor calling a function: 7.2
"""

from time import monotonic
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
import urllib.request

URLS = [
    "http://www.eltiempo.com/",
    "http://www.elpais.com.co/",
    "http://www.bbc.co.uk/",
    "https://www.elmundo.es/",
    "https://es.euronews.com/noticias/internacional",
    "https://www.elespectador.com/",
    "https://www.semana.com/",
    "https://cnnespanol.cnn.com/",
    "https://www.larepublica.co/",
    "https://www.harvard.edu/",
    "https://www.yale.edu/",
    "https://www.utp.edu.co/",
    "http://www.mit.edu/",
    "https://www.stanford.edu/",
    "https://home.www.upenn.edu/",
    "https://duke.edu/",
    "https://www.cornell.edu/",
    "https://www.northwestern.edu/",
    "https://www.rice.edu/",
    "https://www.jhu.edu/",
    "https://wustl.edu/",
    "http://www.emory.edu/",
    "https://www.nd.edu/",
    "https://www.virginia.edu/",
    "https://www.vanderbilt.edu/",
    "https://www.cmu.edu/",
    "https://www.georgetown.edu/",
]


# Retrieve a single page and report the URL and contents
def load_url(url):
    print(f"Loading {url}")
    with urllib.request.urlopen(url, timeout=60) as conn:
        return conn.read()


def load_one_by_one():
    elapsed = monotonic()
    result1 = {url: load_url(url) for url in URLS}
    print(f"\nLoading one by one spent: {(monotonic() - elapsed):.2f}\n")


def load_with_process_pool():
    elapsed = monotonic()
    with ProcessPoolExecutor() as executor:
        result2 = {}
        for url, load in zip(URLS, executor.map(load_url, URLS)):
            result2[url] = load
    print(f"\nProcess Pool Executor spent: {(monotonic() - elapsed):.2f}\n")


def load_with_thread_pool():
    elapsed = monotonic()
    with ThreadPoolExecutor() as executor:
        result3 = {}
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(load_url, url): url for url in URLS}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result3[url] = future.result()
            except Exception as exc:
                print(f"{url} generated an exception: {exc}")
    print(f"\nThread Pool Executor spent: {(monotonic() - elapsed):.2f}\n")


if __name__ == "__main__":
    print(f"Loading {len(URLS)} URLs...")
    load_one_by_one()
    load_with_process_pool()
    load_with_thread_pool()
    print("Done!")
    input("Press Enter to finish...")
