n = int(input())

nums = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(n - i - 1):
        if nums[j] < nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
print(nums)
