s = input()

lst = s.split()
lst_2 = []
c = 0

for i in lst:
    if i.startswith("М"):
        lst_2.append(i)
    elif i.startswith("И"):
        c += 1

print(lst[2:5])
print(lst[3:8])
print(lst_2)
print(c)
