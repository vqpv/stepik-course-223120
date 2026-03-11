d = int(input())
H, M = map(int, input().split())

all_minutes = H * 60 + M + d
hours = (all_minutes // 60) % 24
minutes = all_minutes % 60

print(f"{hours:02d}:{minutes:02d}")
print(f"{H:02d}:{M:02d}")
