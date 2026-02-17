s = input()

print("Есть слова длиной больше 5 символов:", any(len(i) > 5 for i in s.split()))
