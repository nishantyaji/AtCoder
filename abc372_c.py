in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


def read_str_arr(sep=" ") -> list[str]:
    return in_fn().strip().split(sep)


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


def read_2D_str_arr(num_rows, sep=" ") -> list[list[str]]:
    return [read_str_arr(sep) for _ in range(num_rows)]


[n, q] = read_int_arr()
ss = read_str()
queries = read_2D_str_arr(q)

s = list(ss)
flags = [0] * n
res = 0

if n < 3:
    for _ in q:
        op_fn(0)
else:
    for i in range(0, n - 2):
        if s[i] == "A" and s[i + 1] == "B" and s[i + 2] == "C":
            flags[i] = 1
            res += 1

    for x, c in queries:
        x = int(x)
        s[x - 1] = c
        start = max(0, x - 3)
        end = min(x, n - 2)
        for idx in range(start, end):
            if s[idx] == "A" and s[idx + 1] == "B" and s[idx + 2] == "C":
                if flags[idx] == 0:
                    flags[idx] = 1
                    res += 1
            else:
                if flags[idx] == 1:
                    flags[idx] = 0
                    res -= 1
        op_fn(res)
