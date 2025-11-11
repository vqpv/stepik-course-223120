s = input()

a = ord(s[0])
b = ord(s[-1])

print(a)
print(b)
print(str(a) + s[1:-1] + str(b))
