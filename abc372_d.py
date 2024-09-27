in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


num_build = read_int()
heights = read_int_arr()

stack = []
res = [0] * num_build
for i in range(num_build - 1, -1, -1):
    # len(stack) is amount of building that you can see to the right
    # i.e. they are monotonically decreasing till i + 1
    # irrespective of the height of h[i]
    res[i] = len(stack)
    if not stack:
        stack.append((heights[i], i))
    else:
        temp = 0
        while stack and stack[-1][0] < heights[i]:
            (hh, ii) = stack.pop()
        stack.append((heights[i], i))
# use op_fn(*res) instead
op_fn(" ".join(list(map(str, res))))
