n = int(input())

result = 0

for _ in range(n):
    level = int(input())
    if level >= 8:
        result += 1

print(result)
