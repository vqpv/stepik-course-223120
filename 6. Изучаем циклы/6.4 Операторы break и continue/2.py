s = input()

vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
result = ""

for i in s:
    if i in vowels:
        continue
    result += i

print("Очищенное сообщение:", result)
