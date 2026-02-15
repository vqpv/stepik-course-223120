s = input()

print("Все слова начинаются с буквы 'А':", all(i.startswith("А") for i in s.split()))
