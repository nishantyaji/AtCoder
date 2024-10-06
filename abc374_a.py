in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


op_fn("Yes" if read_str()[::-1].startswith("nas") else "No")
