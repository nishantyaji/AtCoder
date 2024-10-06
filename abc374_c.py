import math

in_fn = input
op_fn = print

# A good solution here: https://atcoder.jp/contests/abc374/submissions/58520096

def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num = read_int()
k = read_int_arr()
kset = set(k)
k.sort()

sm = sum(k)
s, e = math.ceil(sm / 2), sm


def calc_(l: list[int]) -> int:
    return sum(list(map(lambda xx: l[xx] * k[xx], list(range(len(k))))))


res = -1
max_val = 2 ** 20 - 1
possible = set()
for i in range(max_val):
    ibin = list(map(int, list(bin(i)[2:].rjust(20, '0'))))
    possible.add(calc_(ibin))

for i in range(s, e):
    if i in possible:
        res = i
        break

op_fn(res)
