#While Loops
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

count = 0
while True:
    print(count)
    count += 1 #infinite loop
    if count >= 5:
        break #Exit the loop
print("Loop ended.")

#continue keywords
count = 0
while count < 5:
    count += 1
    if count == 3: #skip the current iteration
        continue
    print(count)
