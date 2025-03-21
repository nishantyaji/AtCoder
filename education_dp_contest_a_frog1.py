# https://atcoder.jp/contests/dp/tasks/dp_a
import sys

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


n = read_int()
h = read_int_arr()

dp = [sys.maxsize] * n
dp[0] = 0
for i in range(0, n - 1):
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i + 1] - h[i]))
    if i + 2 < n:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(h[i + 2] - h[i]))

op_fn(dp[-1])
