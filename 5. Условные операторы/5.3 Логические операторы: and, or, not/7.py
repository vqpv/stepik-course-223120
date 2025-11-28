a = int(input())
b = int(input())
c = int(input())

if a <= b and c >= 3:
    print("Праздник состоится!")
else:
    if a > b:
        print("Не хватает подарков!")
    elif c < 3:
        print("Недостаточно костюмов снегурочек!")
