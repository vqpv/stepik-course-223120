lst = [i.split(":") for i in input().split()]

result = []

for l in lst:
    if l[2] == "новый":
        result.append(f'{l[0]} {l[1]}')

print(result)
