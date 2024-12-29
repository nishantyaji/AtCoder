import functools
import itertools
import operator
import sys

in_fn = input
op_fn = print


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


[n, k] = read_int_arr()
a = read_int_arr()
all_xor = functools.reduce(operator.xor, a)
if k == n:
    op_fn(all_xor)
    sys.exit()
if k == 1:
    op_fn(max(a))
    sys.exit()
if k == n - 1:
    op_fn(max([all_xor ^ x for x in a]))
    sys.exit()
this_max = 0
negate = False
if k > n // 2:
    negate = True
    k = n - k
for p in itertools.combinations(a, k):
    temp = functools.reduce(operator.xor, p)
    if negate:
        temp = temp ^ all_xor
    this_max = max(this_max, temp)
op_fn(this_max)
