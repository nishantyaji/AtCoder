in_fn = input
op_fn = print


def read_str() -> str:
    return in_fn().strip()


def read_int() -> int:
    return int(in_fn().strip())


num_dim = read_int()
grid = []
for _ in range(num_dim):
    grid.append(list(read_str()))

for x in range(0, num_dim // 2):
    for y in range(x, num_dim - x - 1):
        cells = [[x, y], [y, num_dim - 1 - x], [num_dim - 1 - x, num_dim - 1 - y], [num_dim - 1 - y, x]]
        cell_vals = list(map(lambda ll: grid[ll[0]][ll[1]], cells))

        for k in range(len(cells)):
            grid[cells[k][0]][cells[k][1]] = cell_vals[(k - (x + 1) + 4) % 4]

for rr in range(num_dim):
    op_fn("".join(grid[rr]))
