#Lists
my_list = [1, "Hello", 3.14]
print(my_list)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #嵌套列表
print(nested_list)

print(my_list[0]) #索引
print(my_list[1])

print(my_list[-1]) #负索引，从末尾开始计数
print(my_list[-2])

print(nested_list[0])
print(nested_list[0][0]) #first element of the frst sub-list

# Incorporating in Calculations
numbers = [10, 20, 30]
sum = numbers[0] + numbers[1] 
print(sum)

# Using in Strings (String Formatting)
fruits = ["apple", "banana", "cherry", "pear", "blueberry"]
message = "My favorite fruit is {}.".format(fruits[2])
print(message)  

list_length = len(fruits)
print(list_length)  

fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange" #change list elements
print(fruits)  

fruits.append("mango")
print(fruits)  

fruits.insert(1, "kiwi")
print(fruits)  

other_fruits = ["grape", "pineapple"]
fruits.extend(other_fruits)
print(fruits)  

fruits.remove("kiwi")
print(fruits) 

removed_fruit = fruits.pop(1)
print(removed_fruit)  # Output: "orange"
print(fruits)  

del fruits[0]
print(fruits) 

fruits.clear()
print(fruits) 

#Sorting Lists
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

fruits = ["apple", "kiwi", "orange", "cherry", "mango", "grape", "pineapple", "banana"]
sorted_fruits = sorted(fruits, reverse=True)
print(sorted_fruits)  

fruits.sort(reverse=True)
print(fruits)

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.reverse()
print(numbers)  

fruits = ["apple", "kiwi", "orange", "cherry", "mango", "grape", "pineapple", "banana"]
fruits.sort(key=len)  # Sorting by length of word
print(fruits) 

