# https://atcoder.jp/contests/dp/tasks/dp_e

import sys

in_fn = input
op_fn = print


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


[n, w] = read_int_arr()

w_v = []
for _ in range(n):
    w_v.append(read_int_arr())

w_v.sort(key=lambda x: x[1])
# dp[#num items][value]
sum_v = sum(map(lambda x: x[1], w_v))
dp = []

# We need to find the min in knapsack problem for any given set.
# We need to find the dp[first i items][value=j], find the largest value in the dp[-1] rows that is <= given weight

# The  "minimum weight for given values is the inverse" of "maximize value given weight"
# By minimizing weight on constant values: Knapsack2
# By maximizing values on constant weight: Knapsack1 / Classic knapsack
for _ in range(n + 1):
    dp.append([sys.maxsize] * (sum_v + 1))

for i in range(1, n + 1):
    dp[i][w_v[i - 1][1]] = w_v[i - 1][0]

for i in range(1, n + 1):
    for j in range(1, sum_v + 1):
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        # We do not consider dp[i][j-1] because
        # it stands for the max weight for first i elements with value as j. Having value j - 1 breaks the rule.
        # However, we can choose dp[i-1][j]
        if j >= w_v[i - 1][1]:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - w_v[i - 1][1]] + w_v[i - 1][0])  # similar to classic Knapsack

# We scan from the end of the array till we find an index that has weight just less than or equal to w
temp = 0
for i in range(len(dp[-1]) - 1, -1, -1):
    if dp[-1][i] <= w:
        temp = i
        break
op_fn(temp)
