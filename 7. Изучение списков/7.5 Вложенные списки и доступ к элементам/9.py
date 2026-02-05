map_grid = [
    ["S", "P", "P", "S", "C"],
    ["P", "T", "P", "P", "P"],
    ["P", "P", "S", "C", "P"],
    ["T", "P", "P", "P", "S"],
    ["C", "S", "P", "T", "P"]
]

a, b = input().split()

a = int(a)
b = int(b)

if 0 <= a <= 4 and 0 <= b <= 4:
    c = map_grid[a][b]
    if c == "C":
        print("Сокровище найдено!")
    elif c == "T":
        print("Вы попались в ловушку!")
    elif c == "P":
        print("Продолжайте путь.")
    elif c == "S":
        print("Непроходимая стена.")
else:
    print("Неверные координаты.")
