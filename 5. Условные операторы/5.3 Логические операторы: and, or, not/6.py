a = int(input())
b = int(input())
c = int(input())

if a < 500:
    print("Недостаточно солдат!")
elif a > b * 2:
    print("Недостаточно оружия!")
elif c >= 70 or a > 1000:
    print("Армия готова к битве!")
else:
    print("Низкая мораль армии!")
