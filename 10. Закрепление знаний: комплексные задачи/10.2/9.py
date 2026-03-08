s_1 = input()
s_2 = input()

lst_1 = s_1.split()
lst_2 = s_2.split()

result = []

for i in lst_2:
    for j in lst_1:
        if i == j:
            result.append(i)

if result:
    print("Совпадение найдено:", *result)
else:
    print("Нет совпадений")
