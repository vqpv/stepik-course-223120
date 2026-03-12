p = int(input())

lst = []

for _ in range(p):
    a, b = map(float, input().split())
    lst.append(a * b)

print(lst.index(max(lst)))
