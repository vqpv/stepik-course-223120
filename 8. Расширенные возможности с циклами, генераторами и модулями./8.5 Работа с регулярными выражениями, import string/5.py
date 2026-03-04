import string


s = input()

t = str.maketrans("", "", string.punctuation)
new_s = s.translate(t)
lower_s = new_s.lower()
title_s = lower_s.title()

print(title_s)
