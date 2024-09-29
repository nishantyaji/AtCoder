in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


s = read_str()
mp = {c: i for i, c in enumerate(s)}
prev = 'A'
res = 0
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    res += abs(mp[c] - mp[prev])
    prev = c
op_fn(res)
