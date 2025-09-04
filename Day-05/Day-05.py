# fruits = ["apple", 'Peach','Pear']
# for fruits in fruits:
#     print(fruits + " Pie")
       
# students_scores = [150,142,185,120,111,100,99,200]

# total_exam_score = sum(students_scores)
# print(total_exam_score)

# sum = 0 

# for score in students_scores:
#     sum += score
    
# print(f"Total score is {sum}")

# maximum_score = max(students_scores)
# max = 0 
# for marks in students_scores:
#     if marks > max:
#         max = marks

# #the above code is standard code for finding maximum value in a list
# print(f"The highest score in the class is: {max}")


# students_scores = [150,142,185,120,111,100,99,200]

# sum = 0

# for i in range(1,101): #1 to n-1 
#     sum += i
# print(sum)

# for i in range(1,101):
#     if i%3!=0 and i%5!=0:
#         print(i)
#     elif i%15==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
    
    


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n")) 
import random 
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

password_list = []
for char in range(1,nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1,nr_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1,nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password=''.join(password_list)

random.suffle(password_list)

print(f"Your password is: {password}")