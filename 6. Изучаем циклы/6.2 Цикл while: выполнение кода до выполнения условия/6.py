s = input()

number_of_men = 0
number_of_women = 0

while s != "стоп":
    if "мужчина" in s:
        number_of_men += 1
    elif "женщина" in s:
        number_of_women += 1
    s = input()

print("Количество мужчин:", number_of_men)
print("Количество женщин:", number_of_women)
