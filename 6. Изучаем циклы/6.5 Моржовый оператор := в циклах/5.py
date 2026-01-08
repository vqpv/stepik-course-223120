s = input()

result = ""

l = (len(s) + 1) // 2

s_1 = s[:l][::-1]
s_2 = s[l:][::-1]

for i in range(l - 1):
    result += s_1[i] + s_2[i]

if len(s) % 2 == 0:
    result += s_1[-1] + s_2[-1]
else:
    result += s_1[-1]

print(result)
