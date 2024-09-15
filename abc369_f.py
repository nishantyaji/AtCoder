in_fn = input
op_fn = print


def read_int() -> int:
    return int(in_fn().strip())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


class SegmentTree:
    def __init__(self, size: int):
        # size = size of compressed map (= 1 + max_elem_of_compressed_map)
        self.size = size
        self.st = [(0, 0)] * (4 * size)
        self.invalid = (-100001, -10001)

    def seg_op(self, left: tuple, right: tuple) -> tuple:
        if left[0] > right[0]:
            return left
        elif left[0] == right[0] and left[1] < right[1]:
            return left
        else:
            return right

    def update(self, place_and_index: tuple, val: int):
        self._update_(0, 0, self.size - 1, place_and_index, val)

    def _update_(self, index: int, low: int, high: int, place_and_index: tuple, val: int):
        if low == high:
            if val > self.st[index][0]:
                self.st[index] = val, place_and_index[1]
            return
        mid = (low + high) // 2
        if low <= place_and_index[0] <= mid:
            self._update_(2 * index + 1, low, mid, place_and_index, val)
        else:
            self._update_(2 * index + 2, mid + 1, high, place_and_index, val)

        self.st[index] = self.seg_op(self.st[2 * index + 1], self.st[2 * index + 2])

    def query(self, l_query: int, r_query: int):
        return self._query_(0, 0, self.size - 1, l_query, r_query)

    def _query_(self, index: int, low: int, high: int, l_query: int, r_query: int):
        if low >= l_query and high <= r_query:
            return self.st[index]
        if high < l_query or low > r_query:
            return self.invalid
        mid = (low + high) // 2
        low_val = self._query_(2 * index + 1, low, mid, l_query, r_query)
        high_val = self._query_(2 * index + 2, mid + 1, high, l_query, r_query)
        return self.seg_op(low_val, high_val)


[rows, cols, coins] = read_int_arr()
coords = []
for n_t in range(coins):
    [x, y] = read_int_arr()
    coords.append((x, y))

coords.sort(key=lambda x: (10 ** 6) * x[0] + x[1])

# Approach here is similar to Longest Increasing Subsequence
# Problem no 300 in leetcode
# My implementation:
# https://github.com/nishantyaji/leetcode/blob/main/0300_LongestIncreasingSubsequence.py

# Compressed starts from x:i and not x: i+1 since segment tree is 0-indexed
compressed = {x: i for i, x in enumerate(sorted(set(map(lambda x: x[1], coords))))}
st = SegmentTree(len(compressed))

# This segment-tree times out even for python users,
# even though update and query operations are of O(logn)
# While it passes for C++ ones. :((

memo = []
for i, t in enumerate(coords):
    val = st.query(0, compressed[t[1]])
    memo.append(val)
    # Need to pass the index from enumerate here
    # so that we can from the chain from the beginning till the end
    # and so can form the directions from "D" and "R"
    st.update((compressed[t[1]], i), 1 + val[0])

fnl = st.query(0, len(compressed))

elems = []
prev_val, prev_idx = fnl[0], fnl[1]
while prev_val > 0:
    elems.append(coords[prev_idx])
    [prev_val, prev_idx] = memo[prev_idx]
elems.reverse()


def get_str(press: tuple, prevv: tuple) -> str:
    down = press[0] - prevv[0]
    right = press[1] - prevv[1]
    l = (["D"] * down) + (["R"] * right)
    return "".join(l)


prev = (1, 1)
result = ""
for pres in elems:
    result += get_str(pres, prev)
    prev = pres
result += get_str((rows, cols), prev)
op_fn(fnl[0])
op_fn(result)
