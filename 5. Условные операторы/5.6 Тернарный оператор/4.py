a = float(input())

print("Экстремально холодно" if a < -60 else "Холодно" if -60 <= a <= 0 else "Тепло")
