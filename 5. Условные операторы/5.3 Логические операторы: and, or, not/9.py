a = input()
b = input()
c = input()

if c == "нет":
    print("Рекомендуется выделить больше времени для обучения")
elif a == "да" and b == "да" and c == "да":
    print("Рекомендуется программа: PROкод: курс по ООП на Python")
elif a == "да" and b == "нет" and c == "да":
    print("Рекомендуется программа: PROкод: продвинутый курс по Python")
elif a == "нет" and b == "да" and c == "да":
    print("Рекомендуется программа: Python Professional")
elif a == "нет" and b == "нет" and c == "да":
    print("Рекомендуется программа: PROкод: курс по Python для начинающих")
else:
    print("Рекомендуется программа: PROкод: курс по Python для начинающих")
