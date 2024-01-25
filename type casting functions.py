number = 42
converted_to_string = str(number)
print(f"Number {converted_to_string} is now a string.")
print(type(converted_to_string))

float_number = 3.6
converted_to_int = int(float_number)
print(f"int {converted_to_int}")

float_number = 3.6
converted_to_int = int(float_number)
print(f"Float {float_number} is converted to integer {converted_to_int}.")
# Output: Float 3.6 is converted to integer 3.
# <class 'int'>

string_number = "10.5"
converted_to_float = float(string_number)
print(f"String '{string_number}' is converted to float {converted_to_float}.")
print(type(converted_to_float))
