nums = list(map(float, input().split()))

average_value = sum(nums) / len(nums)

l_1 = [i for i in nums if i < average_value]
l_2 = [i for i in nums if i > average_value]

print(len(l_1), len(l_2))
