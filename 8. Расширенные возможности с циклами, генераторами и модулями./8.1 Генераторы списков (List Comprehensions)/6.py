lst = [x.split() for x in input().split(", ")]
result = []

for l in lst:
    c = False
    for i in l:
        if int(i) >= 50:
            c = True
            break
    if not c:
        result.append(l)

print(result)
