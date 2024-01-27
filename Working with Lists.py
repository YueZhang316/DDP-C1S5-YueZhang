#Working with Lists
for i in range(5):
    print(i)

for i in range(2, 6):
    print(i)

for i in range(0, 10, 2): #range(start, stop, step)逐步递增
    print(i)

numbers = range(5)
print(numbers)
print(list(numbers))

numbers = list(range(5))
print(numbers)

#working with numerical lists
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)

smallest_number = min(numbers)
largest_number = max(numbers)
print(smallest_number)
print(largest_number)

squared_numbers = [x**2 for x in numbers] #new_list = [expression for item in iterable]
print(squared_numbers)

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

parity = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(parity)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced = numbers[2:5]
print(sliced)

first_three = numbers[:3]
last_three = numbers[-3:]
print(first_three)  
print(last_three)  

every_second = numbers[::2] #::从序列开头到序列结束
print(every_second)

reversed_numbers = numbers[::-1]
print(reversed_numbers)

subset = numbers[-5:-2]
print(subset)

for number in numbers[2:6]: #not include index 6
    print(number)

original_list = [[1, 2, 3], [4, 5, 6]]
copied_list = original_list.copy()

copied_list[0][0] = 100
print(original_list)  # Output: [[100, 2, 3], [4, 5, 6]]
print(copied_list)    # Output: [[100, 2, 3], [4, 5, 6]]

from copy import deepcopy

original_list = [[1, 2, 3], [4, 5, 6]]
copied_list = deepcopy(original_list)

copied_list[0][0] = 100
print(original_list)  # Output: [[1, 2, 3], [4, 5, 6]]
print(copied_list)    # Output: [[100, 2, 3], [4, 5, 6]]

import copy
original_list = [[1, 2, 3], [4, 5, 6]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[0][0] = 100
print(original_list)
print(deep_copied_list)
