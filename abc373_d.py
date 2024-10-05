import collections
import platform

in_fn = input
op_fn = print

input_file = platform.node() and platform.node().startswith("LAPTOP-")
if input_file:
    filename = "abc373_d.txt"
    f = open(filename, "r")
    in_fn = f.readline


    def check_file(args):
        exp = f.readline().strip()
        if str(args) == exp:
            print("Pass")
        else:
            print("Fail. Expected:", exp, "Got", args)


    op_fn = check_file


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().strip().split(sep)))


def read_2d_int_arr(num_rows, sep=" ") -> list[list[int]]:
    return [read_int_arr(sep) for _ in range(num_rows)]


[n, m] = read_int_arr()
edges = read_2d_int_arr(m)

adj = collections.defaultdict(dict)
for [out_, in_, w] in edges:
    adj[out_][in_] = w
    adj[in_][out_] = -w

# Note that there can be many connected components
# Also after fixing a node in a connected component
# fixes the other node in the connected component
res = [0] * n
visited = set()
q = []
for i in range(1, n + 1):
    j = i
    if i in visited:
        continue
    res[j - 1] = 0
    q.append(j)

    while q:
        # If you do q.pop() it is DFS. It is more optimal
        # If you do q.pop(0) it is BFS. It is not optimal
        # q.pop(0) is of O(n)
        # q.pop() is of O(1) time complexity
        j = q.pop()
        w = res[j - 1]
        visited.add(j)
        for nei in adj[j].keys():
            if nei not in visited:
                res[nei - 1] = res[j - 1] + adj[j][nei]
                q.append(nei)

op_fn(" ".join(list(map(str, res))))
# op_fn(*res)
