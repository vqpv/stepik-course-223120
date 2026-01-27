n = int(input())

locations = []

for _ in range(n):
    location = input()
    locations.append(location)

target_location = input()

if target_location in locations:
    print(f'Индекс "{target_location}": {locations.index(target_location)}')
else:
    print("Местоположение не найдено.")
