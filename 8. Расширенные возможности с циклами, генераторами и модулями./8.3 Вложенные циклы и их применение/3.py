B = int(input())
W = int(input())
S = int(input())

result = []

for i in range(B):
    s = 0
    for j in range(W):
        s += S
    result.append(s)

print("Количество солдат, прошедших через каждый бастион:", result)
