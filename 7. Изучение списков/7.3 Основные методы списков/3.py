hunters = ['Дон', 'Сим', 'Андрей', 'Богги', 'Кастиель', 'Ребекка']

i = int(input())

if i <= 5:
    hunters.insert(i, 'Джин')
    print("Итоговый список охотников:", hunters)
else:
    print("Неверный индекс!")
