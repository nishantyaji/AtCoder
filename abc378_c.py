nn = int(input().strip())
a = list(map(int, input().strip().split()))

my_dict = {}
res = []
for i, x in enumerate(a):
    res.append(my_dict[x] if x in my_dict else -1)
    my_dict[x] = i + 1
print(*res)
