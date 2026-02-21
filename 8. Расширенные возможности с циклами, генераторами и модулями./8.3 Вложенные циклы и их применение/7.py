s = input()

lst = s.split(", ")

for l in lst:
    for _ in range(len(l)):
        print(l)
