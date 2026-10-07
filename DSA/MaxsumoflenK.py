nums = [2, 5, 4, 2, 1, 5, 3, 6, 1]
k = 3

window_sum = 0

for i in range(k):
    window_sum += nums[i]

max_sum = window_sum

for i in range(k, len(nums)):
    window_sum = window_sum + nums[i] - nums[i - k]

    max_sum = max(max_sum, window_sum)

print(max_sum)