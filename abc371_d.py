import bisect
import itertools

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


n = read_int()
x = read_int_arr()
p = read_int_arr()
num_q = read_int()
queries = []
offset = 0
if x[0] < 0:
    offset = -x[0]

for _ in range(num_q):
    [l, r] = read_int_arr()
    queries.append([l + offset, r + offset])

if x[0] < 0:
    x = [x_ + offset for x_ in x]

pref = list(itertools.accumulate(p))
for [l, r] in queries:
    l_idx = bisect.bisect_left(x, l)
    r_idx = bisect.bisect_left(x, r)
    if r_idx == 0:
        if x[r_idx] == r:
            op_fn(pref[0])
        else:
            op_fn(0)
        continue
    if r_idx == len(x) or x[r_idx] > r:
        r_idx -= 1

    if l_idx == 0:
        op_fn(pref[r_idx])
    else:
        op_fn(pref[r_idx] - pref[l_idx - 1])
