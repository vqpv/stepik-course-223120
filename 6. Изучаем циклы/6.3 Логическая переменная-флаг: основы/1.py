s = input()

flag = False

for i in s:
    if i == "@":
        flag = True

print("Да" if flag else "Нет")
