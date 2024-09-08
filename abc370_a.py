in_fn = input
op_fn = print


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().split(sep)))


arr = read_int_arr()

if sum(arr) in [0, 2]:
    op_fn("Invalid")
elif arr[0] == 1:
    op_fn("Yes")
else:
    op_fn("No")
