class Student :
   def __init__(self,name,age=21, class_no=12):
      self.__name = name
      self.__age = age
      self.__class_no = class_no  

   def set_age (self,age):
      if isinstance(age,int) and age > 0:
         self.__age = age

   def get_age (self):
      print(self.__age) 


class Animal :
  def make_sound(self):
     print("Animal makes sound")

class Dog(Animal):
   def make_sound(self):
      print("Dog Barks")

# animal = Animal()
# animal.make_sound()
# dog = Dog()
# dog.make_sound()


class Calculator :
   def add(self,a,b):
      return a+b
   
   def add(self,a,b,c=0):
      return a+b+c
   
   def add(self,a,b,c=0,d=0):
      return a+b+c+d

sum = Calculator()
print(sum.add(2,3,4,5)) 


from abc import ABC , abstractmethod

class vehicle(ABC):
   @abstractmethod
   def no_of_wheels(self):
      pass

   @abstractmethod
   def str_eengine(self):
      pass

class Bike(vehicle):
   def no_of_wheels(self):
      print("Bike has 2 wheels")

   def str_eengine(self):
      print("Bike has a single cylinder engine")