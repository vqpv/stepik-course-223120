s = input()

alphabet_lowercase = "abcdefghijklmnopqrstuvwxyz"
alphabet_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

new_s = ""
for i in s:
    if i in alphabet_lowercase:
        new_s += alphabet_lowercase[(alphabet_lowercase.index(i) + 3) % 26]
    elif i in alphabet_uppercase:
        new_s += alphabet_uppercase[(alphabet_uppercase.index(i) + 3) % 26]
    else:
        new_s += i

print(new_s)
