import bisect
import functools

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


@functools.cache
def primes_list():
    limit = 1000000
    flags = [0] * (limit + 1)
    flags[1] = flags[0] = 1

    for i in range(2, 1001):
        if flags[i] == 0:
            for j in range(2, 1 + 1000001 // i):
                if i * j <= limit:
                    flags[i * j] = 1

    return [i for i in range(1000001) if flags[i] == 0]


@functools.cache
def special():
    primes = primes_list()
    flags = [0] * 1000001
    for i in range(len(primes)):
        for j in range(2, 1 + 1000000 // primes[i]):
            if primes[i] * j <= 1000000:
                flags[primes[i] * j] += 1
    return [x * x for x in range(1000001) if flags[x] == 2]


num_tests = read_int()
tests = []
for _ in range(num_tests):
    tests.append(read_int())

specials = special()
for num in tests:
    idx = bisect.bisect_left(specials, num)
    res = specials[idx] if idx < len(specials) and specials[idx] == num else specials[idx - 1]
    op_fn(res)
