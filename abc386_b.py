in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


s = read_str()
res = 0
prev = "~"
for i in range(len(s)):
    if s[i] == "0" and prev == "0":
        prev = "~"
        continue
    prev = s[i]
    res += 1

op_fn(res)
