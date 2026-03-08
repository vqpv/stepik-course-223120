nums = list(map(int, input().split(", ")))

stack = [(0, len(nums) - 1)]

while stack:
    left, right = stack.pop()
    if left < right:
        pivot = nums[right]
        i = left - 1
        for j in range(left, right):
            if nums[j] > pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        stack.append((left, i))
        stack.append((i + 2, right))

print(nums)
