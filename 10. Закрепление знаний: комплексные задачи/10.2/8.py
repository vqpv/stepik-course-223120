s = input()

minutes = sorted(list(map(int, s.split())))

print(minutes)
print(f"Ближайший поезд уходит через {minutes[0]} минут")
