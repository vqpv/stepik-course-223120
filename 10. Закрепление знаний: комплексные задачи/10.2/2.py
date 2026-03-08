X = int(input())

if X > 0:
    if X > 500:
        print("Огромная улика")
    else:
        print("Средняя улика")
elif X < 0:
    print("Подозрительный минус")
elif X == 0:
    print("Нулевая зацепка")
