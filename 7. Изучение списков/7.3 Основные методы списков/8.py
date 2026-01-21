ingredients = ["мука", "сахар", "яйца"]

i_1 = input()
i_2 = input()

ingredients.insert(1, i_1)

if i_2 not in ingredients:
    print(f"Ингредиент '{i_2}' не найден в списке.\nОбновлённый список ингредиентов: {ingredients}")
else:
    ingredients.remove(i_2)
    print(f"Ингредиент успешно удалён.\nОбновлённый список ингредиентов: {ingredients}")
