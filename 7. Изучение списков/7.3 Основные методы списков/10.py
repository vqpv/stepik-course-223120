plants = ["дуб", "сосна", "берёза"]

plants_2 = input().split(", ")

plants.extend(plants_2)
print(f"Растения {plants_2} добавлены в список.")

plant = input()

if plant in plants:
    plants.remove(plant)
    print(f"Растение '{plant}' удалено из списка.")
else:
    print(f"Растение '{plant}' не найдено в списке.")

print("Обновлённый список растений:", plants)
