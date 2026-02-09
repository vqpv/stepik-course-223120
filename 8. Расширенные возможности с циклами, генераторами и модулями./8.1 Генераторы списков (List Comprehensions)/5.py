n = int(input())

lst = [f"{i}-{j}" for i in range(1, n + 1) for j in range(1, n + 1)]

print("Координатная карта сокровища:", lst)
