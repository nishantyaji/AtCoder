in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().split(sep)))


n = read_int()
grid = []
for _ in range(n):
    grid.append(read_int_arr())

val = 1
for i in range(1, n + 1):
    min_ = min([i, val])
    max_ = max([i, val])
    val = grid[max_ - 1][min_ - 1]
op_fn(val)
