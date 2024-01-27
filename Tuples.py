#Tuples
my_tuple = (1, "Hello", 3.14)
print(my_tuple[1])

#update Tuples
original_tuple = (1, 2, 3)
new_tuple = (original_tuple[0], 4, original_tuple[2]) #第一个位置的元素是 original_tuple 中的第一个元素，第二个位置的元素是4，第三个位置的元素是 original_tuple 中的第三个元素
original_tuple = new_tuple
print(original_tuple)

original_tuple = (1, 4, 3)
print(original_tuple)  
original_tuple = (1, 2, 3)
print(original_tuple)
