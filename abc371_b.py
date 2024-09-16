in_fn = input
op_fn = print


def read_str_arr(sep=" ") -> list[str]:
    return in_fn().strip().split(sep)


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


# n families, m babies
[n, m] = read_int_arr()
res = []
st = set()
for _ in range(m):
    [family, gender] = read_str_arr()
    if gender == "M" and family not in st:
        res.append("Yes")
        st.add(family)
    else:
        res.append("No")

for r in res:
    op_fn(r)
