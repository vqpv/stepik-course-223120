total_distance = 100000000
current_distance = 0
daily_travel = 1

while current_distance < total_distance and daily_travel > 0:
    daily_travel = int(input())
    if daily_travel <= 0:
        break
    current_distance += daily_travel
    print(f"Текущая пройденная дистанция: {current_distance} км")

if current_distance >= total_distance:
    print("Ура! Экспедиция успешно добралась до планеты!")
else:
    print("Экспедиция прервана. До Новой Земли так и не долетели...")
