n = int(input())
s_1 = input()
s_2 = input()

c = 0

lst_1 = list(map(float, s_1.split()))
lst_2 = list(map(float, s_2.split()))

for i in range(n):
    if lst_1[i] > lst_2[i]:
        c += 1

print(c)
