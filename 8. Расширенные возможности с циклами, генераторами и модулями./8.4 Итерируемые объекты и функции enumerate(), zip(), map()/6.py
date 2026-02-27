s_1 = input()
s_2 = input()

for i, j in zip(s_1.split(", "), s_2.split(", ")):
    print(i, j)
