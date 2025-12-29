n = int(input())

flag = False
i = 0

while not flag and i < n:
    x = int(input())
    if x < 0:
        flag = True
        print(f"Найдено отрицательное на позиции {i}")
    i += 1

if not flag:
    print("Отрицательных нет")
