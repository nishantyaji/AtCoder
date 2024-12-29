in_fn = input
op_fn = print


def read_str_arr(sep=" ") -> list[str]:
    return in_fn().strip().split(sep)


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


class BIT:
    def __init__(self, size: int):
        self.size = size
        self.bit = [0] * (size + 1)

    def update(self, place: int, val: int):
        while place <= self.size:
            self.bit[place] += val
            place += (place & -place)

    def query(self, place: int) -> int:
        result = 0
        while place > 0:
            result += self.bit[place]
            place -= (place & -place)
        return result


[rows, queries] = read_int_arr()
vals = []
for _ in range(queries):
    s = read_str_arr()
    t = (int(s[0]), int(s[1]), s[2])
    vals.append(t)
res = True

vals.sort(key=lambda x: (x[0], x[1], x[2]))  # sort by rows

cols = set(list(map(lambda x: x[1], vals)))
mp = {x: i + 1 for i, x in enumerate(sorted(cols))}
fw = BIT(len(vals) + 1)
for i in range(len(vals)):
    if vals[i][2] == "W":
        fw.update(mp[vals[i][1]], 1)
    else:
        cnt = fw.query(mp[vals[i][1]])
        if cnt > 0:
            res = False
            break

op_fn("Yes" if res else "No")
