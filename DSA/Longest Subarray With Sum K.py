nums = [10, 5, 2, 7, 1, 9]
k = 15

prefix_sum = 0
length = 0

seen = {}

for i in range(len(nums)):
    prefix_sum += nums[i]

    if prefix_sum == k:
        length = max(length, i + 1)

    if prefix_sum - k in seen:
        length = max(length, i - seen[prefix_sum - k])
        
    if prefix_sum not in seen:
        seen[prefix_sum] = i

print(length)