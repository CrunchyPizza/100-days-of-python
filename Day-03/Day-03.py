#program to check if number is even or not
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("This is an even number.")
# else: 
#     print("This is an odd number.")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height>=120: 
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age<12:
#         print("Child tickets are $5.")
#     elif age<=18:
#         print("Youth tickets are $7.")    
#     else:
#         print("Youth tickets are $12.")
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         if age<12:
#             print("Your total bill is $5 + $3 = $8.")
#         if age<=18:
#             print("Your total bill is $7 + $3 = $10.")
#         if age>18:
#             print("Your total bill is $12 + $3 = $15.")
#     else:
#         if age<12:
#             print("Your total bill is $5.")
#         if age<=18:
#             print("Your total bill is $7.")
#         if age>18:
#             print("Your total bill is $12.")            

# else: 
#     print("Sorry, you have to grow taller before you can ride. ")     

# Alternative way

# print("Welcome to the rollercoaster!")
# bill = 0
# height = int(input("What is your height in cm? "))
# if height>=120: 
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age<12:
#         print("Child tickets are $5.")
#         bill = 5
#     elif age<=18:
#         print("Youth tickets are $7.")    
#         bill = 7
#     else:
#         print("Youth tickets are $12.")
#         bill = 12

#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#         print(f"Your total bill is ${bill}.")
#     else:
#         print(f"Your total bill is ${bill}.")
# else: 
#     print("Sorry, you have to grow taller before you can ride. ")     

# print("Welcome to Python Pizza Deliveries!")
# size = input("What is the size of the group? S, M, or L? ").upper()
# pepperoni = input("Do you want pepperoni? Y or N ").upper()
# extra_cheese = input("Do you want extra cheese? Y or N ").upper()
# bill = 0 
# if size=="S":
#     bill+=15
#     if pepperoni=="Y":
#         bill+=2
#         if extra_cheese=="Y":
#             bill+=1
#     if pepperoni=="N":
#         if extra_cheese=="Y":
#             bill+=1             
#     print(f"Your final bill is: ${bill}.")    
    
# elif size=="M":
#     bill+=20
#     if pepperoni=="Y":
#         bill+=3
#         if extra_cheese=="Y":
#             bill+=1
#     if pepperoni=="N":
#         if extra_cheese=="Y":
#             bill+=1             
#     print(f"Your final bill is: ${bill}.")
    
# else: 
#     bill+=25
#     if pepperoni=="Y":
#         bill+=3
#         if extra_cheese=="Y":
#             bill+=1
#     if pepperoni=="N":
#         bill+=3
#         if extra_cheese=="Y":
#             bill+=1             
#     print(f"Your final bill is: ${bill}.")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What is the size of the group? S, M, or L? ").upper()
# pepperoni = input("Do you want pepperoni? Y or N ").upper()
# extra_cheese = input("Do you want extra cheese? Y or N ").upper()
# bill = 0 
# if size == "S": 
#     bill += 15
# elif size == "M":
#     bill +=20
# elif size == "L": 
#     bill +=25
# else: 
#     print("Invalid size.")
# if pepperoni == "Y":
#     if size == "S":
#         bill +=2
#     else:
#         bill +=3
# if extra_cheese == "Y":
#     bill +=1

# print(f"Your final bill is ${bill}.")

print("Welcome to the rollercoaster!")
bill = 0
height = int(input("What is your height in cm? "))
if height>=120: 
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age<12:
        print("Child tickets are $5.")
        bill = 5
    elif age<=18:
        print("Youth tickets are $7.")    
        bill = 7

    elif 45<=age<=55:
        print("Everything is going to be ok. Have a free ride on us!")
        bill = 0
    else:
        print("Youth tickets are $12.")
        bill = 12
    

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
        print(f"Your total bill is ${bill}.")
    else:
        print(f"Your total bill is ${bill}.")
else: 
    print("Sorry, you have to grow taller before you can ride. ")     
