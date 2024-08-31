num_elems = int(input())
arr = list(map(int, input().split()))


def val_(n: int):
    return (n * (n + 1)) // 2 - (2 * n - 1)


res = 2 * num_elems - 1
if num_elems > 2:
    d = arr[1] - arr[0]
    num_ap = 2
    for i in range(2, len(arr)):
        now_d = arr[i] - arr[i - 1]
        if d == now_d:
            num_ap += 1
        else:
            d = now_d
            if num_ap > 2:
                res += val_(num_ap)
            num_ap = 2

    if num_ap > 2:
        res += val_(num_ap)

print(res)
