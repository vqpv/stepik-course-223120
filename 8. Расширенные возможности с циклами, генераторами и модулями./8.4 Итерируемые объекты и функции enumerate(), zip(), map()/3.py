s_1 = input()
s_2 = input()

lst_1 = s_1.split()
lst_2 = s_2.split()

for i, j in enumerate(lst_1, start=1):
    for w in lst_2:
        if w == j:
            print(f'Слово "{w}" найдено на позиции {i}')
            break
