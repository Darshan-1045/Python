s = "abcabcbb"

uniqueEle = set()
left = 0
right = 0
maxLength = 0 

while right < len(s) :

  if s[right] not in uniqueEle :
    uniqueEle.add(s[right])
    right += 1
    maxLength = max(maxLength,right - left)
  else :
    uniqueEle.remove(s[left])
    left += 1

print(maxLength)



