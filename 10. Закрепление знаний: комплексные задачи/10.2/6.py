s = input()

lst = list(map(int, s.split()))

result = [l for l in lst if l > 1000]

if result:
    for i in result:
        print(i)
else:
    print("Нет крупных переводов")
