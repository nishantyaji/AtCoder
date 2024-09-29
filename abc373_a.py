in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


res = 0
for i in range(1, 13):
    s = read_str()
    if i == len(s):
        res += 1
op_fn(res)
