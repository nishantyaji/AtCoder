[n, k] = map(int, input().strip().split())
s = list(input().strip())

question = "?"
dot = "."
o_char = "o"


def override(start: int, end: int):
    for j in range(start, end + 1):
        s[j] = o_char if (j - start) % 2 == 0 else dot


def get_ind_blocks(start: int, end: int):
    if (end - start + 1) % 2 == 1:
        return (end - start + 2) // 2, True
    return (end - start + 1) // 2, False


for i, x in enumerate(s):
    if x == o_char:
        k -= 1
        if i > 0 and s[i - 1] == question:
            s[i - 1] = dot
        if i < len(s) - 1 and s[i + 1] == question:
            s[i + 1] = dot

if k > 0:
    op, close = -1, -1
    blocks = []
    for i, x in enumerate(s):
        if x == question:
            if op < 0:
                op = i
            close = i
        else:
            if op >= 0:
                blocks.append((op, close))
            op, close = -1, -1

    if op >= 0:
        blocks.append((op, close))

    total = 0
    for b in blocks:
        sub_total, is_sure = get_ind_blocks(b[0], b[1])
        total += sub_total

    if total == k:
        for b in blocks:
            sub_total, is_sure = get_ind_blocks(b[0], b[1])
            if is_sure:
                override(b[0], b[1])
else:
    for i in range(len(s)):
        if s[i] == question:
            s[i] = dot
print("".join(s))
