lst = [i for i in input().split(", ")]

result = []

for l in lst:
    a, b = l.split(":") 
    if float(a) > 0.8 and int(b) < 50:
        result.append(l)

print(result)
