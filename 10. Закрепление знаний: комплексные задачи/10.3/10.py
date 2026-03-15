values = list(map(float, input().split()))

print(min(values), max(values), sum(values))
print("Возрастают" if values == sorted(values) and all(values.count(i) == 1 for i in values) else "Не возрастают")
