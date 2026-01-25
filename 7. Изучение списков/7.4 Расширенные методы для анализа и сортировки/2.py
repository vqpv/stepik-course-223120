n = int(input())

lst = []

for _ in range(n):
    name = input()
    lst.append(name)

favorite_title = input()

print(lst.index(favorite_title) if favorite_title in lst else "Фильм не найден в коллекции.")
print(lst.count(favorite_title))
