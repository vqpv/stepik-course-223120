P, n, r = map(float, input().split())

S = P * (1 + r / 100) ** n

print(S)
