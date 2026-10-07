# l = [2,4,3,5,8,3,4]
# new = []


# sum = 0

# print(l)

# for i in range(0,len(l)):
#   new.append(l[i] * 2)

# print(new)

# marks = {"darshi" : "43",
#          "manoj" : "48",
#          "sampth" : "46",
#          "karthi" : "41",
#          "aroodha" : "45"
#          }

# for name,marks in marks.items() : 
#   print(name,marks)

name = ["Darsi",
        "manoj",
        "sampth",
        "karthi",
        "aroodha"]

marks = [23,23,12,32,32]

# student_marks = {}

# for i in range(len(marks)) :
#  student_marks[name[i]] = marks[i]

# nmae = ["darshi","deepak","prakasha","jyothi"]

# upper = [value.upper() for value in nmae]

# print(upper)

'''The video 11 home work'''

'''
# problem one

foods = ["dose","idli","rice","palav"]

upper_foods = [food.upper() for food in foods]

print(upper_foods)

'''
'''

# problem 2

ball = {
         "ball1" : 24 ,
         "ball2" : 27 ,
         "ball3" : 30 ,
         "ball4" : 35 ,
         "ball5" : 20 
       } 

total = 0

for item in ball.values() :
   total += item

print(total)

'''


#problem 3

'''

list = [i for i in range(1,11)]

print(list)

squares = [num**2 for num in list]

print(squares)

'''


# problem 4

'''

matrix = [[1,2,3],[4,5,6],[7,8,9]]

for row in matrix :
     sum = 0
     for j in row :
          sum += j
     print(sum)

'''

# detail = [{
#            "Name" : "Darshan" ,
#            "age" : 23,
#            "Marks" : 45},
#           {
#            "Name" : "Darshan" ,
#            "age" : 23,
#            "Marks" : 45
#            },
#            {
#            "Name" : "Darshan" ,
#            "age" : 23,
#            "Marks" : 45
#            }
#          ]

# for student in detail :
#   print(student.items())


# population cities

cities ={
         "Bengaluru" : 60 ,
         "Chitradurga" : 9 ,
         "Mysuru" :15,
         "Bidar" : 8,
         "Davanagere" : 12     
        }

populated = {city : pop for city,pop in cities.items() if pop > 10}

print(populated)
           


          
   
    