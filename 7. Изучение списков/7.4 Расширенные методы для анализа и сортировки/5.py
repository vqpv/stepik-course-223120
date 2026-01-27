m = int(input())

locations = []
lst = []

for _ in range(m):
    locations.append(input())

for location in locations:
    if location not in lst:
        lst.append(location)

for l in lst:
    print(f"{l}:", locations.count(l))
