in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


def read_int() -> int:
    return int(in_fn().strip())


slen = read_int()
s = read_str()
res = 0
for i in range(1, slen - 1):
    if s[i] == "." and s[i - 1] == "#" and s[i + 1] == "#":
        res += 1

op_fn(res)
