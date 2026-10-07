nums = [2, 3, 1, 2, 4, 3]
k = 7
sum = 0
left = 0
min_length = float('inf')

for right in range(len(nums)) :
  sum += nums[right]

  while sum >= k :
    min_length = min(min_length, right - left + 1)
    sum -= nums[left]
    left += 1

result = min_length if min_length != float('inf') else 0

print(result)

