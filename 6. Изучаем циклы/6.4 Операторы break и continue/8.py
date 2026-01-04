c = 0
nums = ""

while True:
    s = input()
    if s.isdigit():
        if int(s) == 0:
            print(c)
            print(nums.rstrip(", "))
            break
        elif int(s) > 0:
            nums += s + ", "
            continue
        else:
            c += 1
            continue
    else:
        c += 1
        continue
