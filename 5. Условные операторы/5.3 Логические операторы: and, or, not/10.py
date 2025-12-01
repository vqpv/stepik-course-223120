age = int(input())
status = input()
rating = int(input())
membership = input()
invitation = input()

if age < 18:
    print("Недостаточный возраст")
elif status not in ["разработчик", "дизайнер"]:
    print("Неверный профессиональный статус")
elif invitation == "да":
    print("Доступ разрешен")
elif rating > 80:
    print("Доступ разрешен")
elif 50 <= rating <= 80 and membership == "да":
    print("Доступ разрешен")
else:
    print("Недостаточный рейтинг")
