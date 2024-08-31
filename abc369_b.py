num_lines = int(input())
val = []
hand = []
for n_t in range(num_lines):
    ins = input().split()
    val.append(int(ins[0]))
    hand.append(ins[1])

prev_L = -1
prev_R = -1

effort = 0
for i in range(len(val)):
    if hand[i] == "L":
        if prev_L != -1:
            effort += abs(val[i] - prev_L)
        prev_L = val[i]
    elif hand[i] == "R":
        if prev_R != -1:
            effort += abs(val[i] - prev_R)
        prev_R = val[i]

print(effort)
