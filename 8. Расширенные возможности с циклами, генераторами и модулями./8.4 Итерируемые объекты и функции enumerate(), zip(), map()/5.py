lst_1 = input().split()
lst_2 = input().split()

print([int(i) + int(j) for i, j in zip(lst_1, lst_2)])
