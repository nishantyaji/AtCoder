ls = list(map(int, input().split()))
if ls[0] == ls[1]:
    print(1)
elif (ls[0] + ls[1]) % 2 == 0:
    print(3)
else:
    print(2)
