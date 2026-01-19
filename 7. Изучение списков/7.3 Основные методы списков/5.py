hunters = ['Джин', 'Дон', 'Сим', 'Андрей', 'Богги', 'Кастиель']

i = int(input())

if i in range(len(hunters)):
    hunters.pop(i)
    print("Обновленный список охотников:", hunters)
else:
    print("Неверный индекс!")
