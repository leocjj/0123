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
from time import monotonic
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
]
"""    
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
]"""


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


def calculate_one_by_one():
    elapsed = monotonic()
    result = []
    for prime in PRIMES:
        result.append(is_prime(prime))
    print(f"\tfor loop spent: {(monotonic() - elapsed):.2f}")


def calculate_with_list_comprehension():
    elapsed = monotonic()
    result = [is_prime(prime) for prime in PRIMES]
    print(f"\tList comprehension spent: {(monotonic() - elapsed):.2f}")
    return result


def calculate_with_list_map():
    elapsed = monotonic()
    result = list(map(is_prime, PRIMES))
    print(f"\tList map spent: {(monotonic() - elapsed):.2f}")
    return result


def calculate_with_process_pool(workers):
    elapsed = monotonic()
    with ProcessPoolExecutor(max_workers=workers) as executor:
        result = []
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            result.append(prime)
    print(f"\tProcess Pool Executor spent: {(monotonic() - elapsed):.2f}")
    return result


def calculate_with_thread_pool(workers):
    elapsed = monotonic()
    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_if_prime = {executor.submit(is_prime, prime): prime for prime in PRIMES}
        result = []
        for future in as_completed(future_if_prime):
            number = future_if_prime[future]
            try:
                result.append(future.result())
            except Exception as exc:
                print(f"{number} generated an exception: {exc}")
    print(f"\tThread Pool Executor spent: {(monotonic() - elapsed):.2f}")
    return result


if __name__ == "__main__":
    print(f"\nCalculating {len(PRIMES)} primes...\n")
    calculate_one_by_one()
    calculate_with_list_comprehension()
    calculate_with_list_map()
    for workers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
        print(f"\nWorkers: {workers}")
        calculate_with_thread_pool(workers)
        calculate_with_process_pool(workers)

    print("\n")
