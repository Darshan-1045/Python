nums = [2, 7, 11, 15]

target = 9

present = False 

needs = {}

for num in nums :
  need = target - num 
  if need in needs :
    print(needs[need],nums.index(num)) 
    present = True

  needs[num] = nums.index(num)

if not present : 
  print("not present")