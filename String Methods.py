#String Methods

#upper and lower case
text = "Python is fun!"
upper_text = text.upper()
print(upper_text)

lower_text = text.lower()
print(lower_text)

# String with leading and trailing whitespace
whitespace_string = "  Hello, Python!  "

# Removing whitespace
stripped_string = whitespace_string.strip()
print(stripped_string)


sentence = "I like apples."

#Finding a substring
index = sentence.find("apples")
print(index)

#Replacing a substring
new_sentence = sentence.replace("apples", "oranges")
print(new_sentence)

#Splitting a string
data = "apple, banana, cherry"
fruits = data.split(",")
print(fruits)

#Joining a list of strings
sentence = " ".join(fruits)
print(sentence)


