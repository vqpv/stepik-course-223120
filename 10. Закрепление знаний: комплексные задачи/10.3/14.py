s_1 = input()
s_2 = input()
s_3 = input()

lst = s_1.split() + s_2.split() + s_3.split()

for i, j in enumerate(lst):
    print(f"{i}-{j}")
