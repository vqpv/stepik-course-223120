s = input()

lst = []

for i in s.split():
    lst.append(int(i))

print(lst[:-2])
print(lst[-2:])
