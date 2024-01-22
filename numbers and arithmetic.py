positive_integer = 10
negative_integer = -5

positive_float = 10.5
negative_float = -3.14

print(5 + 2) #Addition
print(5 - 2) #Subtraction
print(5 * 2) #Multiplication
print(5 / 2) #Division
print(5 // 2) #Floor Division
print(5 % 2) #Modulus
print(5 ** 2) #Exponentiation

print(4 + 2.0)
print(8 / 4) #Always results in a float.
print(7 // 2)

billion = 1_000_000_000

#Calculate the square foot of a number.
import math
square_root = math.sqrt(16)
print(square_root)

#Generate a random integer wihin a specified range.
import random
random_integer = random.randint(1, 10)
print(random_integer)

age = input("Enter your age: ")
age = int(age)
print("You are", age, "years old.")