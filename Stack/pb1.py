class stack :
  def __init__(self) :
    self.items = []

  def push(self,val) :
    self.items.append(val)

  def pop(self) :
    if len(self.items) == 0 :
      return "Cannot pop Element because Stack is EMPTY"
    else :
      x = self.items.pop()
      return x

  def top(self) :
    if len(self.items) == 0 :
      return "Cannot give top Element because Stack is EMPTY"
    else :
     return self.items[-1]

  def size(self) :
    return len(self.items) 

  def is_empty(self) :
    return len(self.items) == 0

  def print(self) :
    return self.items


nums = stack()

nums.push(1)
nums.push(2)
nums.push(3)
nums.push(4)

print(nums.top())
print(nums.pop())
print(nums.print())
print(nums.is_empty())
print(nums.size())



  