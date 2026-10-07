class human :
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def info(self):
    print(f"The age of {self.name} is {self.age}")

class Student : 
  def __init__ (self,name,marks,subject):
    self.name = name
    self.marks = marks
    self.subject = subject

  def info(self):
    print(f"The marks of {self.name} in the {self.subject} is {self.marks}")

darshan = human("Darshan",22)
S1 = Student("Darshan",97,"Mathematics")

darshan.info()
S1.info()


class Movie :
  def __init__(self,title="unknown",ratings=0):
    self.title = title
    self.ratings = ratings

  def about(self) :
    print(f"The title of the movie is {self.title} and the ratings are {self.ratings} for 5")


# Toxic = Movie("Toxic",4.5)
# Toxic.about()

# jai = Movie()

# jai.about()

class Employee :
  def __init__(self,name,designation = "SDE", salary = 35000):
    self.name = name
    self.designation = designation
    self.salary = salary

  def info(self) :
    print(f"The name of the employee is {self.name} and the designation is {self.designation} and the salary is {self.salary}")

Chandan = Employee("Chandan", "SDE-1", 40000)
Chandan.info()
Darshan = Employee("Darshan")
Darshan.name = "Deepak bro"
Darshan.info()

