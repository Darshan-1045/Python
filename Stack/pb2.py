# Stack using the Queue

from collections import deque

class stack_using_queue :
  def __init__(self) :
    self.queue = deque()

  def push(self,val) :
    self.queue.append(val)
    for _ in range(len(self.queue) - 11) :
      self.queue.append(self.queue.popleft())

  def pop(self) : 
     if len(self.queue) == 0 :
      return " unable to do "
     else :
      x = self.queue.popleft()
      return x
   