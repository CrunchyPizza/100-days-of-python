# print("Welcome to the tip calculator.")
# total_bill = float(input("What was the total bill? $"))
# tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# number_of_people = int(input("How many people to split the bill? "))
# tip_as_percent = tip_percentage / 100
# total_tip_amount = total_bill * tip_as_percent
# total_bill_with_tip = total_bill + total_tip_amount
# bill_per_person = total_bill_with_tip / number_of_people

# final_amount = "{:.2f}".format(bill_per_person) #Idk
# print(f"Each person should pay: ${final_amount}")
      

# print("Hello"[0]) #H
# print("Hello"[4]) #o
# print("Hello"[-1]) #o
# print("Hello"[-2]) #l

# print("Hello"[0:3]) #Hel
# print("Hello"[1:4]) #ell
# print("Hello"[0:5]) #Hello 
# print("Hello"[0:6]) #Hello

#Integer = whole number 
# print(123_789) #we can use _ in between numbers to make it more readable

#Float = decimal number 

# print(3.14159)

# decimal point floating thus flaot.

#Boolean = True or False.

# print(1)
# print(0)

# len(12345) #Error
#len() function only works with string type error

# len("12345") #5

# len("Hello World") #11


# print(type("Hello")) #str
# print(type(123)) #int
# print(type(123.456)) #float
# print(type(True)) #bool
# print(type(False)) #bool


# print(int("123"))

# print(int("float")) #Value Error

# int()
# float()
# str()
# bool()


#print("Number of letters in your name: " + str(len((input("What is your name?")))))

#=================================================================================================
# Mathematical Operators

# print("My age: " + str(2025 - 2008))
# print(123+456)
# print(7-3)
# print(3*2)
# print(5//3)
# print()



# print(3*(3 + 3)/3 -3 ) 
# bmi = 84/1.65**2
# print(round(bmi,2))

# score= 0 
# score+=0

#f-String

# Score = 0 
# height = 1.8 
# is_winning = True

# print(f"Your score is {Score}, your height is {height}, you are winning is {is_winning}")


# tip calculator
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $" ) ) 
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? ") )
number_of_people = int(input("How many people to split the bill? ") )
tip_as_percent = tip_percentage / 100
total_tip_amount = total_bill * tip_as_percent
total_bill_with_tip = total_bill + total_tip_amount
bill_per_person = total_bill_with_tip / number_of_people

rounded_bill = round(bill_per_person,2)

print(f"Each person should pay: ${rounded_bill}")


