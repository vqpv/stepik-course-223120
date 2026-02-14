s = input()

print("Все числа положительные:", all(int(i) > 0 for i in s.split()))
