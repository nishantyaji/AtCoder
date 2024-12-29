import collections

in_fn = input
op_fn = print


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


x = collections.Counter(read_int_arr())
res = False
if len(x) == 2:
    vals = set(x.values())
    set1, set2 = {2}, {1, 3}
    res = True if vals == set1 or vals == set2 else False
op_fn("Yes" if res else "No")
