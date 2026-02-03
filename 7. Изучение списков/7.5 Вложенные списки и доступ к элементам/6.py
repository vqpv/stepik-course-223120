inventory = [
    ["Меч", "Топор", "Лук"],
    ["Зелье здоровья", "Зелье маны"],
    ["Дерево", "Камень", "Железо"]
]

s_1 = input()
s_2 = input()

inventory_copy_1 = inventory.copy()
inventory_copy_2 = []

for i in inventory:
    inventory_copy_2.append(i.copy())

inventory_copy_1[0].append(s_1)
inventory_copy_2[0].append(s_2)

print("Оригинальный инвентарь:", inventory)
print("Поверхностная копия:", inventory_copy_1)
print("Глубокая копия:", inventory_copy_2)
