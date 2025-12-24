secret = 37

c = 1
n = int(input())

while n != secret:
    c += 1
    if n > secret:
        print("Слишком много!")
    else:
        print("Слишком мало!")
    n = int(input())

print("Код верный, темница открыта!")
print("Количество попыток:", c)
