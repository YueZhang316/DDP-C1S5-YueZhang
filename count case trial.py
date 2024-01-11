def case_counter(text):
    uppercase_count = 0
    lowercase_count = 0

    # Iterate through each character in the input string
    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    # Return the counts
    return f"Uppercase letters: {uppercase_count}, Lowercase letters: {lowercase_count}"

# Test cases
print(case_counter("Hello World!"))
print(case_counter("PYTHON"))
print(case_counter("python"))
print(case_counter("1234!@#$"))
