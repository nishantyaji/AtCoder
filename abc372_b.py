in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


m = read_int()
i = -1
res = []
j = 10
while j >= 0 and m > 0:
    bs = 3 ** j
    q, r = divmod(m, bs)
    if q >= 1:
        to_rem = min(q, 10)
        m = m - to_rem * bs
        res += [j] * to_rem
    else:
        j -= 1
op_fn(len(res))
op_fn(" ".join(list(map(str, res))))
