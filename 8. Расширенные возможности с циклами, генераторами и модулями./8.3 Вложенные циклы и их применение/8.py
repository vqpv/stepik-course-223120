s_1 = input()
s_2 = input()

for i in s_1.split():
    for j in s_2.split():
        if i == j:
            print(i)
            break
