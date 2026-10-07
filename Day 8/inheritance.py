"""

class vehicle :
  def __init__ (self,vehicle_type):
    self.__vehicle_type = vehicle_type

  def start(self) :
   print(f"{self.__vehicle_type} is starting.") 

  def type(self) :
    print(f"This is a {self.__vehicle_type}.")

class bike(vehicle) :
  def __init__ (self,vehicle_type,brand):
    super().__init__(vehicle_type)
    self.__brand = brand

  def start(self) :
    print(f"{self.__brand} {self.__vehicle_type} is starting")


honda = bike("bike","Honda")

honda.type()
"""

# polymorphism

class shape :
  def area(self) :
    print("Area of shape is undefined")

class rectangle(shape) :
  def __init__(self,length,breadth) :
    self.__length = length
    self.__breadth = breadth

  def area(self) :
    return self.__length * self.__breadth

class circle(shape) :
  def __init__(self,radius) :
    self.__radius = radius

  def area(self) :
    return 3.14 * self.__radius ** 2


shapes = [rectangle(5,10),circle(7)]

for shape in shapes :
  print(f"Area: {shape.area()}")
