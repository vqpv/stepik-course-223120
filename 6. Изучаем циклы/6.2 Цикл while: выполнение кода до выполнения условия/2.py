secret_number = 7

s = 0
n = int(input())

while n != secret_number:
    s += n
    n = int(input())

print("Вы угадали!", s)
