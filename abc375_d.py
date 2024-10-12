import collections

in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


s = read_str()
my_dict = collections.defaultdict(list)
cntr = collections.Counter(s)
res = 0
for i, c in enumerate(s):
    if len(my_dict[c]) > 0:
        pres_len = len(my_dict[c])
        rem = cntr[c] - pres_len
        res += (i - my_dict[c][-1] - 1) * (rem * pres_len)  # when present c is not chosen
        res += (rem - 1) * pres_len  # when present c is chosen
    my_dict[c].append(i)

op_fn(res)
