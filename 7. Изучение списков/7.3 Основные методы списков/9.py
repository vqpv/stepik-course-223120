destinations = ["Париж", "Рим", "Барселона"]

for _ in range(3):
    city = input()
    if city in destinations:
        print(f"Город '{city}' уже есть в списке.")
    else:
        destinations.append(city)
        print(f"Город '{city}' добавлен в список.")

print("Обновлённый список направлений:", destinations)
