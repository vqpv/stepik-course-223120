s = input()

print(len(s))

count = s.count(" ")
print(count)

if count > 5:
    print("Слишком много пропусков!")
else:
    print("Нормально")
