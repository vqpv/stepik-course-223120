hunters = ['Джин', 'Дон', 'Сим', 'Андрей', 'Богги', 'Кастиель', 'Ребекка']

name = input()

if name in hunters:
    hunters.remove(name)
    print("Обновленный список охотников:", hunters)
else:
    print("Такого охотника нет в списке.")
