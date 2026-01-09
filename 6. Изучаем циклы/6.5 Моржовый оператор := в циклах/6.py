mushrooms_in_basket = 0

while mushrooms_in_basket < 50:
    n = int(input())
    if n <= 0:
        print("Вы решили завершить тихую охоту.")
        break
    else:
        mushrooms_in_basket += n
        if mushrooms_in_basket > 50:
            print("Корзина переполнена!")
            mushrooms_in_basket = 50
            break
        else:
            print(f"Сейчас в корзине: {mushrooms_in_basket} грибов")

print(f"Итоговое количество грибов в корзине: {mushrooms_in_basket}")
