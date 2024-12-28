import bisect
import platform

in_fn = input
op_fn = print

input_file = platform.node() and platform.node().startswith("LAPTOP-")
if input_file:
    filename = "abc376_c.txt"
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


num = read_int()
a = read_int_arr()
b = read_int_arr()

a.sort()
b.sort()

failures = []
while b:
    idx = bisect.bisect_right(a, b[-1])
    if idx == 0:
        b.pop()
    elif idx < len(a):
        failures += a[idx:]
        a = a[:idx]
    else:
        b.pop()
        a.pop()

failures = failures if len(failures) else a
res = -1 if len(failures) > 1 else failures[0]
op_fn(res)
