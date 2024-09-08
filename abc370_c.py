in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


s = read_str()
t = read_str()

m = 0
for i in range(len(s)):
    if s[i] != t[i]:
        m += 1


def get_next(source: str, target: str):
    return_str = ""
    flag = False
    for j in range(len(source)):
        if not flag and source[j] > target[j]:
            return_str += target[j]
            flag = True
        else:
            return_str += source[j]

    if not flag:
        return_str = ""
        another_flag = False
        for j in range(len(source) - 1, -1, -1):
            if not another_flag and source[j] < target[j]:
                return_str = target[j] + return_str
                another_flag = True
            else:
                return_str = source[j] + return_str
    return return_str


op_fn(m)
for i in range(m):
    s = get_next(s, t)
    op_fn(s)
