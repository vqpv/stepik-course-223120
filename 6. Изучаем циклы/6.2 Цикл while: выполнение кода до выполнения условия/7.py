s = input()
result = 0

while s != "хватит":
    if s.isdigit():
        num_1 = float(s)
        operator = input()
        if operator in ("+", "-", "*", "/"):
            num_2 = float(input())
            if operator == "+":
                result = num_1 + num_2
                print("Результат:", result)
            elif operator == "-":
                result = num_1 - num_2
                print("Результат:", result)
            elif operator == "*":
                result = num_1 * num_2
                print("Результат:", result)
            elif operator == "/":
                if num_2 != 0:
                    result = num_1 / num_2
                    print("Результат:", result)
                else:
                    print("Ошибка: деление на ноль невозможно.")
        else:
            print("Неверный оператор")
    s = input()

print("Работа калькулятора завершена.")
