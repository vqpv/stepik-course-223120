N, M = input().split()

N = int(N)
M = int(M)

grades = []

c_1 = 0
c_2 = 0

for i in range(N):
    s = input().split()
    grades.append([])
    for j in range(M):
        num = int(s[j])
        if num % 2 == 0:
            c_1 += 1
        else:
            c_2 += 1
        grades[i].append(num)

print("Четных чисел:", c_1)
print("Нечетных чисел:", c_2)
