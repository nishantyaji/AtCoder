import math

in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


def read_2d_int_arr(num_rows, sep=" ") -> list[list[int]]:
    return [read_int_arr(sep) for _ in range(num_rows)]


num_tests = read_int()
coords = read_2d_int_arr(num_tests)
coords = [[0, 0]] + coords
coords += [[0, 0]]

res = 0
for i in range(len(coords) - 1):
    x2 = (coords[i][0] - coords[i + 1][0]) * (coords[i][0] - coords[i + 1][0])
    y2 = (coords[i][1] - coords[i + 1][1]) * (coords[i][1] - coords[i + 1][1])
    res += math.sqrt(x2 + y2)
op_fn(res)
