a = int(input())
b = input()
c = input()
d = input()

if a < 20:
    print("Вольер слишком мал!")
elif b == "да" and c == "нет":
    print("Вода нужна для водных животных!")
elif d == "нет":
    print("Вольер небезопасен!")
else:
    print("Вольер подходит!")
