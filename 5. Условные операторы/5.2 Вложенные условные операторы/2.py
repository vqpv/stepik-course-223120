x, y, z = input().split()

y = float(y)
z = float(z)

r = 0
c = 1
p_1 = 200
p_2 = 500
p_3 = 1000


if x == "обычная":
    if y <= 5:
        r = p_1
    elif 5 < y <= 20:
        r = p_2
    elif y > 20:
        r = p_3
elif x == "срочная":
    if z <= 100:
        c = 1.10
    elif z > 100:
        c = 1.15
    if y <= 5:
        r = p_1 * c
    elif 5 < y <= 20:
        r = p_2 * c
    elif y > 20:
        r = p_3 * c

print(f"Стоимость доставки: {round(r)} рублей.")
