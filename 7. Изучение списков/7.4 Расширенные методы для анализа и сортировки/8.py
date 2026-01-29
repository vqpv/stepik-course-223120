q = int(input())

lst = []

for _ in range(q):
    lst.append(input())

l = input()

lst_copy = lst.copy()

print(lst)
print(lst_copy)

lst_copy.append(l)

print(lst)
print(lst_copy)
