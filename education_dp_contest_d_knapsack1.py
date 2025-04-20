# https://atcoder.jp/contests/dp/tasks/dp_b

in_fn = input
op_fn = print


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


[n, w] = read_int_arr()

w_v = []
for _ in range(n):
    w_v.append(read_int_arr())

w_v.sort(key=lambda x: x[0])

# dp[#num items][weight]

dp = []
for _ in range(n + 1):
    dp.append([0] * (w + 1))

for i in range(1, n + 1):
    dp[i][w_v[i - 1][0]] = w_v[i - 1][1]

for i in range(1, n + 1):
    for j in range(1, w + 1):
        dp[i][j] = max(dp[i][j], dp[i][j - 1], dp[i - 1][j])
        if w_v[i - 1][0] <= j:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w_v[i - 1][0]] + w_v[i - 1][1])

op_fn(dp[-1][-1])
