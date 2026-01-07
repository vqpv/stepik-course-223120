N = 100
c = 0

while True:
    if c < N:
        c += (n := int(input()))
        print(f"Суммарно собрано: {c} ягод")
    else:
        print("Достаточно ягод для варенья! Возвращаемся домой.")
        break
