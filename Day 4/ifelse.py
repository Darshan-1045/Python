# Gender = input("enter your gender : ")
# Age = int(input("Enter your Age : "))

# if Gender == "Female":
#   print("Ticket is free...")
# else:
#   if Age < 5:
#     print("ticket is free")
#   elif Age <= 12 and Age > 5 :
#     print("children discount")  
#   elif Age >= 60:
#     print("you get senior citizen dizcount")
#   else :
#     print("you need to pay full")

time = input("Enter the time in 24 hr format : ") # time like 1,2,3,4,.......,23,24.

if time == "8":
  print("it's time for Breakfast")
elif time == "13":
  print("it's time for Lunch")
elif time == "20":
  print("it's time for Dinner")
else :
  print("it's not time for food or it's not meal time")