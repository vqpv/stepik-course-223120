lst = [j.split(":") for j in [i for i in input().split()]]

lst_x, lst_y = [], []

for l in lst:
    x, y = int(l[0]), int(l[1])
    if 0 < x < 100 and 0 < y < 100:
        lst_x.append(x)
        lst_y.append(y)

print("X:", lst_x)
print("Y:", lst_y)
