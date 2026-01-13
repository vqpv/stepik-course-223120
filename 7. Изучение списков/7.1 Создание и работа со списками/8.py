s = input()

lst = s.split()

lst_2 = []
c = 0

for i in lst:
    if i.startswith("Г"):
        lst_2.append(i)
    elif i.startswith("М"):
        c += 1

print(lst[2:5])
print(lst_2)
print(c)
