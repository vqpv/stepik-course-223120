n = int(input())

nums_1 = list(map(float, input().split()))
nums_2 = list(map(float, input().split()))

c = 0

for i in range(n):
    if nums_1[i] > nums_2[i]:
        c += 1

print(int((c / n) * 100))
