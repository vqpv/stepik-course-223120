hunters = ['Дон', 'Сим']

lst = []

while True:
    s = input()
    if s == "стоп":
        break
    lst.append(s)

s = input()
lst_2 = s.split(", ")

hunters.extend(lst)
hunters.extend(lst_2)

print("Итоговый список охотников:", hunters)
