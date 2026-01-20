hunters = ['Джин', 'Дон', 'Сим', 'Андрей', 'Кастиель']

name = input()

if name in hunters:
    hunters.remove(name)
    print("Монстр удалён. Обновленный список:", hunters)
else:
    print("Монстр не найден в списке.")
