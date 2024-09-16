import collections
import itertools
import platform
import sys

in_fn = input
op_fn = print

input_file = platform.node() and platform.node().startswith("LAPTOP-")
if input_file:
    filename = "contest/abc371/abc371_c.txt"
    f = open(filename, "r")
    in_fn = f.readline


    def check_file(args):
        exp = f.readline().strip()
        if str(args) == exp:
            print("Pass")
        else:
            print("Fail. Expected:", exp, "Got", args)


    op_fn = check_file


def read_int() -> int:
    return int(in_fn())


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().split(sep)))


def read_2D_int_arr(num_rows, sep=" ") -> list[list[int]]:
    return [read_int_arr(sep) for _ in range(num_rows)]


num_nodes = read_int()
num_edges_1 = read_int()
edges1 = read_2D_int_arr(num_edges_1)
num_edges_2 = read_int()
edges2 = read_2D_int_arr(num_edges_2)
costs = read_2D_int_arr(num_nodes - 1)

adj1 = collections.defaultdict(set)
for e in edges1:
    adj1[e[0]].add(e[1])
    adj1[e[1]].add(e[0])

adj2 = collections.defaultdict(set)
for e in edges2:
    adj2[e[0]].add(e[1])
    adj2[e[1]].add(e[0])

min_score = sys.maxsize
# We iterate over all possible permutation (as possibilities for H i.e. Graph2)
# Find the cost associated with each permutation
# Find the minimum of the costs
# Given N <= 8. That leaves the complexity to be O(8!) i.e. 40k loops
for p in itertools.permutations(range(1, num_nodes + 1)):
    score = 0
    mp = {i: p[i - 1] for i in range(1, num_nodes + 1)}
    rev = {p[i - 1]: i for i in range(1, num_nodes + 1)}
    for i in range(1, num_nodes + 1):
        orig_neis = adj1[i]
        now_neis = set([rev[x] for x in adj2[mp[i]]])
        to_add = orig_neis - now_neis
        to_remove = now_neis - orig_neis

        to_add_rev = [mp[x] for x in to_add]
        to_remove_rev = [mp[x] for x in to_remove]

        for y in to_add_rev:
            small, large = min(mp[i], y), max(mp[i], y)
            score += costs[small - 1][large - small - 1]
        for y in to_remove_rev:
            small, large = min(mp[i], y), max(mp[i], y)
            score += costs[small - 1][large - small - 1]
    score = score // 2
    min_score = min(min_score, score)

op_fn(min_score)
