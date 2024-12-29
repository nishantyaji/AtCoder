in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


def read_int() -> int:
    return int(in_fn().strip())


k = read_int()
s = read_str()
t = read_str()

res = False

if len(s) == len(t):
    cnt = sum([1 if s[i] != t[i] else 0 for i in range(len(s))])
    if cnt == 1 or cnt == 0:
        res = True
elif abs(len(s) - len(t)) == 1:
    short, long = (t, s) if len(s) > len(t) else (s, t)
    first = -1
    for i in range(len(short)):
        if short[i] != long[i]:
            first = i
            break
    if first == -1:
        first = len(short)
    res = long[first + 1:] == short[first:]

op_fn("Yes" if res else "No")
