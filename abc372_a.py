in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


s = read_str()
op_fn("".join([c for c in s if c != "."]))
