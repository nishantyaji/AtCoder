import platform

in_fn = input
op_fn = print

input_file = platform.node() and platform.node().startswith("LAPTOP-")
if input_file:
    filename = "contest/abc370/abc370_d.txt"
    f = open(filename, "r")
    in_fn = f.readline


    def check_file(args):
        exp = f.readline().strip()
        if str(args) == exp:
            print("Pass")
        else:
            print("Fail. Expected:", exp, "Got", args)


    op_fn = check_file


class SegmentTree:
    def __init__(self, size: int):
        # size = size of compressed map (= 1 + max_elem_of_compressed_map)
        self.size = size
        self.st = [(None, None)] * (4 * size)

    def build(self, nums: list[int]):
        self._build_(0, 0, self.size - 1, nums)

    def _build_(self, index: int, low: int, high: int, nums: list[int]):
        if low == high:
            # self.st[index] = nums[low]
            self.st[index] = (nums[low], nums[low])
            return

        mid = (low + high) // 2
        self._build_(2 * index + 1, low, mid, nums)
        self._build_(2 * index + 2, mid + 1, high, nums)
        self.st[index] = self.seg_op(self.st[2 * index + 1], self.st[2 * index + 2])

    def seg_op(self, left: tuple, right: tuple) -> tuple:
        return self._min_(left[0], right[0]), self._max_(left[1], right[1])

    def _com_(self, a, b):
        if a is None and b is None:
            return None
        elif a is None:
            return b
        elif b is None:
            return a
        return None

    def _min_(self, a, b):
        if a is not None and b is not None:
            return min([a, b])
        else:
            return self._com_(a, b)

    def _max_(self, a, b):
        if a is not None and b is not None:
            return max([a, b])
        else:
            return self._com_(a, b)

    def update(self, place: int, val: int):
        self._update_(0, 0, self.size - 1, place, val)

    def _update_(self, index: int, low: int, high: int, place: int, val: int):
        if low == high:
            # use unary_op below
            self.st[index] = (val, val)
            return
        mid = (low + high) // 2
        if low <= place <= mid:
            self._update_(2 * index + 1, low, mid, place, val)
        else:
            self._update_(2 * index + 2, mid + 1, high, place, val)

        self.st[index] = self.seg_op(self.st[2 * index + 1], self.st[2 * index + 2])

    def query(self, l_query: int, r_query: int):
        return self._query_(0, 0, self.size - 1, l_query, r_query)

    def _query_(self, index: int, low: int, high: int, l_query: int, r_query: int):
        if low >= l_query and high <= r_query:
            return self.st[index]
        if high < l_query or low > r_query:
            return None, None
        mid = (low + high) // 2
        low_val = self._query_(2 * index + 1, low, mid, l_query, r_query)
        high_val = self._query_(2 * index + 2, mid + 1, high, l_query, r_query)
        return self.seg_op(low_val, high_val)


class SpecialSortedSet:
    def __init__(self, nums: list[int]):
        self.sz = len(nums)
        self.st = SegmentTree(self.sz)
        self.st.build(nums)
        self.collection = set(nums)

    def __len__(self):
        return len(self.collection)

    def discard(self, element: int):
        self.remove(element)

    def remove(self, element: int):
        if element in self.collection:
            self.collection.remove(element)
            self.st.update(element, None)
            return True
        return False

    def bounds_cleaned(self, element) -> list[int]:
        result = []
        t = self.bounds(element)
        if t[0] is not None:
            result.append(t[0])
        if t[1] is not None:
            result.append(t[1])
        return result

    def bounds(self, element) -> tuple:
        l_bound = self.st.query(0, element)[1]
        u_bound = self.st.query(element, self.sz)[0]
        return l_bound, u_bound


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().split(sep)))


# SpecialSortedSet: SortedTree implemented with Segment tree but it TLEs

# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
# Check AtCoder Solution: https://atcoder.jp/contests/abc370/submissions/57356652
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional

T = TypeVar('T')


class SortedSet(Generic[T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        n = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        if any(a[i] >= a[i + 1] for i in range(n - 1)):
            a, b = [], a
            for x in b:
                if not a or a[-1] != x:
                    a.append(x)
        n = self.size = len(a)
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [a[n * i // num_bucket: n * (i + 1) // num_bucket] for i in range(num_bucket)]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1: len(s) - 1] + "}"

    def _position(self, x: T) -> Tuple[List[T], int, int]:
        "return the bucket, index of the bucket and position in which x should be. self must not be empty."
        for i, a in enumerate(self.a):
            if x <= a[-1]: break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a, b, i = self._position(x)
        if i != len(a) and a[i] == x: return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b:b + 1] = [a[:mid], a[mid:]]
        return True

    def _pop(self, a: List[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a: del self.a[b]
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x: return False
        self._pop(a, b, i)
        return True

    def lt(self, x: T) -> Optional[T]:
        "Find the largest element < x, or None if it doesn't exist."
        # Lower Bound
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Optional[T]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        "Find the smallest element > x, or None if it doesn't exist."
        # Upper bound
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: return a[i]
        else:
            for a in self.a:
                if i < len(a): return a[i]
                i -= len(a)
        raise IndexError

    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0: return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a): return self._pop(a, b, i)
                i -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


[rows, cols, q] = read_int_arr()
queries = []
for _ in range(q):
    queries.append(read_int_arr())

row_sp = []
for r in range(rows):
    ss = SortedSet(list(range(0, cols)))
    row_sp.append(ss)

col_sp = []
for c in range(cols):
    ss = SortedSet(list(range(0, rows)))
    col_sp.append(ss)

for [r, c] in queries:
    r -= 1
    c -= 1

    flag = c in row_sp[r]
    row_sp[r].discard(c)

    if not flag:
        bonds = [row_sp[r].lt(c), row_sp[r].gt(c)]
        # bonds = row_sp[r].bounds_cleaned(c)
        for b in bonds:
            if b is not None:
                row_sp[r].discard(b)
                col_sp[b].discard(r)

    flag = r in col_sp[c]
    col_sp[c].discard(r)
    if not flag:
        bonds = [col_sp[c].lt(r), col_sp[c].gt(r)]
        # bonds = col_sp[c].bounds_cleaned(r)
        for b in bonds:
            if b is not None:
                col_sp[c].discard(b)
                row_sp[b].discard(c)

res = 0
for i in range(rows):
    res += len(row_sp[i])
op_fn(res)
