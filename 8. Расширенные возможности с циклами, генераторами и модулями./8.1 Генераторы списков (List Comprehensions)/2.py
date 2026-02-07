names = input().split(", ")

lst = [i for i in names if i.startswith("Н")]

print("Имена экипажа, начинающиеся с буквы 'Н':", lst)
