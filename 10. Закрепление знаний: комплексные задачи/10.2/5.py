N = int(input())

a, b = 0, 0

for _ in range(N):
    num = int(input())
    if num % 2 == 0:
        a += num
    else:
        b += num

print("Сумма чётных:", a)
print("Сумма нечётных:", b)

if a > b:
    print("Чётные преобладают")
else:
    print("Нечётные (или равенство)")
