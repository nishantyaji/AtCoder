in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


s = read_str()
t = read_str()
a = s if len(s) < len(t) else t
b = s if a == t else t
# len(b) >= len(a) always
res = 0
for i in range(len(b)):
    if i == len(a) or b[i] != a[i]:
        res = i + 1
        break

op_fn(res)
