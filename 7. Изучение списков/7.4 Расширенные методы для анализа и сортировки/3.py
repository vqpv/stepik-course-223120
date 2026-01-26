m = int(input())

films = []

for _ in range(m):
    films.append(input())

films.sort()
print(films)

films.reverse()
print(films)
