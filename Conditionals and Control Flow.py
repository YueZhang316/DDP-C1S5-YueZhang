#Conditionals and Control Flow
#Booleans
#True
print(bool(1))  
print(bool("hello"))  
print(bool([1, 2, 3]))  
#False
print(bool(0)) 
print(bool("")) 
print(bool(0.0))  
print(bool(0j)) 
print(bool({})) 

#Conditional Tests
#Comparison Operators
x = 10
print(x == 10)  
print(x != 5)   
print(x > 5)    
print(x < 15)   
print(x >= 6)
print(x <= 11)

print("Hello" == "Hello")
print("Hello" == "hello")

print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] == [3, 2, 1])

#Logical Operators
x, y = 10, 20
print(x < 15 and y > 15)
print(x > 15 or y > 15)
print(not x == 10)

#Membership Tests
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)     
print("mango" not in fruits) 

#Identify Tests
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)    
print(a is c)    # False: c is a new list
print(a is not c)  # True

#If Statements
number = 10
if number > 5:
    print("Number is greater than 5.")

number = 24
if number > 25:
    print("Nunber is greater than 25.")
elif number > 20:
    print("Number is greater than 20 but not greater than 25.")
else:
    print("Number is 20 or less.")

age = 18

if age >= 18:
    print("Adult Ticket")
else:
    print("Children Ticket")

score = 75

if score >= 70:
    grade = "Distinction"
elif score >= 60:
    grade = "Merit"
elif score >= 50:
    grade = "Pass"
else:
    grade = "Fail"
print(f"Your grade is {grade}.")