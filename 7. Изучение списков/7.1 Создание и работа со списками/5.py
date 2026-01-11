s = input()

lst = s.split(" ")

nums = []

for i in lst:
    nums.append(int(i))

print(nums)
print((a := sum(nums)) / len(nums))
print(a)
