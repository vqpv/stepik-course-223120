n = int(input())
m = int(input())

matrix = []

for _ in range(n):
    matrix.append(input().split())

orbit_index = int(input())
landing_index = int(input())

print(matrix[orbit_index][landing_index])
