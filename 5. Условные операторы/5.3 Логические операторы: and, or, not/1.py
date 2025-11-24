health = int(input())
has_weapon = input().lower() == "да"
has_armor = input().lower() == "да"

if health > 50:
    if has_weapon or has_armor:
        print("Готов к сражению!")
    else:
        print("Не стоит сражаться без экипировки!")
elif health <= 50:
    if has_weapon and has_armor:
        print("Не стоит рисковать, но у тебя есть все шансы выжить!")
    elif has_weapon or has_armor:
        print("Не стоит рисковать!")
    else:
        print("Не готов к сражению!")
