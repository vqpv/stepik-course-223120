lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

s = input()
shift = int(input())

result = ""

for i in s:
    if i in lowercase:
        result += lowercase[(lowercase.index(i) - shift) % 26]
    elif i in uppercase:
        result += uppercase[(uppercase.index(i) - shift) % 26]
    else:
        result += i

print("Расшифрованное сообщение:", result)
