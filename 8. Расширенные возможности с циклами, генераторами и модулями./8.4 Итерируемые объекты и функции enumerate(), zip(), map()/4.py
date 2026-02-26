lst_1 = input().split()
lst_2 = input().split()

result = []

for i, j in zip(lst_1, lst_2):
    result.append(int(i))
    result.append(int(j))

print(result)
