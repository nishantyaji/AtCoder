# https://atcoder.jp/contests/dp/tasks/dp_c

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


def read_2d_int_arr(num_rows, sep=" ") -> list[list[int]]:
    return [read_int_arr(sep) for _ in range(num_rows)]


n = read_int()
vals = read_2d_int_arr(n)

dp = []
for _ in range(n):
    dp.append([0, 0, 0])

dp[0][0] = vals[0][0]
dp[0][1] = vals[0][1]
dp[0][2] = vals[0][2]

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + vals[i][0]
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + vals[i][1]
    dp[i][2] = max(dp[i - 1][1], dp[i - 1][0]) + vals[i][2]

temp = max(dp[-1])
op_fn(temp)
