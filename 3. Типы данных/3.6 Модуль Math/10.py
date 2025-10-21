from math import radians, sin


v = int(input())
o = int(input())

g = 9.81
r = radians(o)

T = (2 * v * sin(r)) / g
H = (v ** 2 * sin(r) ** 2) / (2 * g)
R = (v ** 2 * sin(2 * r)) / g

print(round(T, 2))
print(round(H, 2))
print(round(R, 2))
