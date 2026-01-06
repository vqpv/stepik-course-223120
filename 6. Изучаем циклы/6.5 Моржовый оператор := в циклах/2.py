total_supplies = 0

while True:
    total_supplies += (supplies := int(input()))
    if total_supplies < 20:
        print(f"Припасов недостаточно! Всего осталось {total_supplies} единиц.")
        break
    else:
        total_supplies -= 20
        continue
