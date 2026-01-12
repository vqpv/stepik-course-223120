s = input()

lst = []

for i in s.split():
    lst.append(int(i))

print(lst[2:5])
print(lst[5:])
print(sum(lst[:4]))
