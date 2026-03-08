s = input()

lst = s.split()
a, b = lst[0], lst[0]

for l in lst:
    if len(a) >= len(l):
        a = l
    if len(b) <= len(l):
        b = l

print(a)
print(b)
