k = int(input())

lst = [input() for _ in range(k)]

for num, name in enumerate(lst, start=1):
    print(f"{num}. {name}")
