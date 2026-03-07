nums = list(map(int, input().split(" ")))

sorted_sublists = [[num] for num in nums]

while len(sorted_sublists) > 1:
    merged_sublists = []
    i = 0
    while i < len(sorted_sublists) - 1:
        left = sorted_sublists[i]
        right = sorted_sublists[i + 1]
        merged = []
        l_i = r_i = 0
        while l_i < len(left) and r_i < len(right):
            if left[l_i] < right[r_i]:
                merged.append(left[l_i])
                l_i += 1
            else:
                merged.append(right[r_i])
                r_i += 1
        while l_i < len(left):
            merged.append(left[l_i])
            l_i += 1
        while r_i < len(right):
            merged.append(right[r_i])
            r_i += 1
        merged_sublists.append(merged)
        i += 2
    if len(sorted_sublists) % 2 == 1:
        merged_sublists.append(sorted_sublists[-1])
    sorted_sublists = merged_sublists

nums = sorted_sublists[0]
print(nums)
