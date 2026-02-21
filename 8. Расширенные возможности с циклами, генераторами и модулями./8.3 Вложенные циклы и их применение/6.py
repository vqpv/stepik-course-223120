while True:
    s = input()
    if s == "STOP":
        break
    if s == s[::-1]:
        print(s)
