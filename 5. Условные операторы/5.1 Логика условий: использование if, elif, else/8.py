n = input()

if not n.isdigit():
    print("Некорректный ввод")
else:
    if int(n) < 0:
        print("Некорректный ввод")
    elif 0 < int(n) < 12:
        print("Привет, малыш!")
    elif 12 <= int(n) <= 18:
        print("Привет, подросток!")
    elif 19 <= int(n) <= 65:
        print("Добрый день, взрослый!")
    elif int(n) > 65:
        print("Здравствуйте, уважаемый пенсионер!")
