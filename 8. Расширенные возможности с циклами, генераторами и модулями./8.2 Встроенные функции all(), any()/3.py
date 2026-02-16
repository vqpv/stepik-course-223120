s = input()

print("Список содержит отрицательные числа:", any(int(i) < 0 for i in s.split()))
