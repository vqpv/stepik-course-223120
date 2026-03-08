s = input()

nums = list(map(int, s.split()))

print(*[i for i in nums if i > 0])
