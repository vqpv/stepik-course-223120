n = int(input())

for _ in range(n):
    flag = False
    login = input()
    for i in login:
        if i.isdigit():
            flag = True
    if flag:
        print(login)
