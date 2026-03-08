s_1 = input()
s_2 = input()

lst = s_1.split()

if s_2 in lst:
    print(lst.index(s_2))
else:
    print(-1)
