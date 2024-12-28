import platform

in_fn = input
op_fn = print

input_file = platform.node() and platform.node().startswith("LAPTOP-")
if input_file:
    filename = "abc376_b.txt"
    f = open(filename, "r")
    in_fn = f.readline


    def check_file(args):
        exp = f.readline().strip()
        if str(args) == exp:
            print("Pass")
        else:
            print("Fail. Expected:", exp, "Got", args)


    op_fn = check_file


def read_str() -> str:
    return in_fn().strip()


def read_int() -> int:
    return int(in_fn().strip())


def read_str_arr(sep=" ") -> list[str]:
    return in_fn().strip().split(sep)


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


def read_2d_int_arr(num_rows, sep=" ") -> list[list[int]]:
    return [read_int_arr(sep) for _ in range(num_rows)]


def read_2d_str_arr(num_rows, sep=" ") -> list[list[str]]:
    return [read_str_arr(sep) for _ in range(num_rows)]


[n, q] = read_int_arr()
queries = read_2d_str_arr(q)

l, r = 1, 2
res = 0
for [h, t] in queries:
    t = int(t)
    if h == "L":
        if l > r > t:
            # example l=10, r=3, t=1
            res += (n - l) + (t - 1) + 1
        elif t > r > l:
            # example l=1, r=3, t=5
            res += (l - 1) + (n - t) + 1
        elif l > t > r:
            # example l=1, r=5, t=2
            res += l - t
        elif r > t > l:
            # example l=5, r=2, t=3
            res += t - l
        elif r > l > t:
            # example r = 10, l = 5, t = 3
            res += l - t
        elif t > l > r:
            # example t = 9, l = 5, r = 1
            res += t - l
    else:
        if r > l > t:
            # example l=3, r=5, t=1
            res += (n - r) + (t - 1) + 1
        elif l > r > t:
            # example l = 5, r = 4, t = 1
            res += r - t
        elif r > t > l:
            # example l = 1, r= 8, t = 5
            res += r - t
            pass
        elif l > t > r:
            # example l = 11, t = 6, r = 2
            res += t - r
        elif t > r > l:
            # example l = 4, r= 5, t = 6
            res += t - r
        elif t > l > r:
            # example l = 7, r = 3, t = 12
            res += (n - t) + (r - 1) + 1

    if h == "L":
        l = t
    else:
        r = t

op_fn(res)
