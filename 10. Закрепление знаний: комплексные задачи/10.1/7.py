s = input()

words = s.split()
a, b = words[0], words[0]

for word in words:
    if len(a) > len(word):
        a = word
    if len(b) < len(word):
        b = word

print(a)
print(b)
