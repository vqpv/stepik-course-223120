k = int(input())

result = []

for _ in range(k):
    lst = list(map(str.lower, input().split()))
    if "H2O".lower() in lst:
        result.append(lst[0])

if result:
    for i in result:
        print(i.upper())
else:
    print("Нет воды")
