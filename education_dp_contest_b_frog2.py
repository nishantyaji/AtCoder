# https://atcoder.jp/contests/dp/tasks/dp_b

import sys

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


[n, k] = read_int_arr()
h = read_int_arr()

dp = [sys.maxsize] * n
dp[0] = 0
for i in range(0, n - 1):
    for j in range(1, k + 1):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + abs(h[i + j] - h[i]))

op_fn(dp[-1])
