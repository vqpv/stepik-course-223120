name = input()
surname = input()

print(f"Добро пожаловать, детектив {name} {surname}!")

answer = input()

if answer.lower() == "да":
    print("Приступаем к осмотру")
elif answer.lower() == "нет":
    print("Хорошо, подождём")
