s = input()

count = len(s.split())

print("Всего подозреваемых:", count)

if count > 5:
    print("Нужно больше людей для допроса")
else:
    print("Справимся своими силами")
