cookies = 7

while True:
    s = input()
    if s.lower() == "стоп":
        print(f"Вы остановились и оставили печеньки на потом.\nНа тарелке осталось {cookies} печенек. Вы остановились раньше.")
        break
    elif s.isdigit():
        x = int(s)
        if 0 < x <= cookies:
            cookies -= x
            print(f"Вы съели {x} печенек. Осталось на тарелке: {cookies}")
            if cookies == 0:
                print("Все печеньки съедены! Приятного аппетита!")
                break
            else:
                continue
        elif x > cookies:
            print(f"Нельзя съесть {x} печенек, ведь осталось всего {cookies}!")
            continue
        elif x <= 0:
            print("Неправильное количество, пропускаем эту попытку.")
            continue
