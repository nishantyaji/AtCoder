num_elems = int(input())
arr = list(map(int, input().split()))

if num_elems == 1:
    print(arr[0])
elif num_elems == 2:
    print(arr[0] + 2 * arr[1])
else:
    dp = [[0 for col in range(2)] for row in range(len(arr))]
    dp[0][1] = arr[0]
    dp[0][0] = 0
    dp[1][0] = arr[0] + 2 * arr[1]
    dp[1][1] = arr[1]

    for i in range(2, len(arr)):
        dp[i][0] = max(dp[i - 1][1] + 2 * arr[i], dp[i - 2][1] + 2 * arr[i])
        dp[i][1] = max(dp[i - 1][0] + arr[i], dp[i - 2][0] + arr[i])

    max0 = max(list(map(lambda x: x[0], dp)))
    max1 = max(list(map(lambda x: x[1], dp)))

    print(max(max1, max0))
