a, b = map(int, input().split())

b_1 = b // 100
b_2 = b // 10 % 10
b_3 = b % 10

print(a % (b_1 + b_2 + b_3) == 0)
