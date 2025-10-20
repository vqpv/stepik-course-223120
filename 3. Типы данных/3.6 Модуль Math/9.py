from math import radians, sin, cos, tan


a = int(input())

r = radians(a)
s = round(sin(r), 6)
c = round(cos(r), 6)
t = round(tan(r), 6)

print(s)
print(c)
print(t)
