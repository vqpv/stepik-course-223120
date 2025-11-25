health = int(input())
mana = int(input())
has_item = input().strip().lower() == "да"

if (health >= 50 and mana > 0) or (health <= 50 and has_item):
    print("Герой готов к битве!")
else:
    print("Герой не готов к битве!")
