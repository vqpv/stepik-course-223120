c = 0

while True:
    if c == 3:
        print("Вы собрали три непустые строки. Задача завершена!")
        break
    s = input()
    if s == "":
        print("Пустая строка, пропускаем...")
        continue
    elif s == "стоп":
        print(f"Сбор строк прерван.\nЗадача завершена досрочно.")
        break
    else:
        c += 1
        print(f"Принято! (строк собрано: {c})")
        continue
