R, C = input().split()

R = int(R)
C = int(C)

grid = []

for i in range(5):
    grid.append(["."] * 5)
    for j in range(5):
        if i == R - 1 and j == C - 1:
            grid[i][j] = "P"
    print(*grid[i])
