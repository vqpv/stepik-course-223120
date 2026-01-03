water_level = 0

while True:
    water_level += 3
    print(f"Вода поднялась, уровень: {water_level}")
    if water_level >= 10:
        print("Пещера затоплена! Вы не успели...")
        break
    else:
        s = input()
        if s == "стоп":
            print(f"Спасательная операция прервана.\nОперация завершена. Текущий уровень воды: {water_level}")
            break
        elif s.isdigit:
            s = int(s)
            if s == 0:
                print("Неположительная откачка, пропускаем...")
                continue
            elif s > 0:
                if water_level >= s:
                    water_level -= s
                    continue
                else:
                    water_level = 0
                    continue
