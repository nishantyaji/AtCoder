in_fn = input
op_fn = print


def read_str_arr(sep=" ") -> list[str]:
    return in_fn().strip().split(sep)


chars = read_str_arr()

# AB AC BC
if chars == [">", ">", ">"]:
    op_fn("B")
elif chars == [">", ">", "<"]:
    op_fn("C")
elif chars == [">", "<", ">"]:
    pass
elif chars == [">", "<", "<"]:
    op_fn("A")
elif chars == ["<", ">", ">"]:
    op_fn("A")
elif chars == ["<", ">", "<"]:
    pass
elif chars == ["<", "<", ">"]:
    op_fn("C")
elif chars == ["<", "<", "<"]:
    op_fn("B")
