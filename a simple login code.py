#try to write a simple login code

def login():
    correct_username = "zhang"
    correct_password = "password123456"

    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    if entered_username == correct_username and entered_password == correct_password:
        print("Login successful! Welcome, " + entered_username + "!")
    else:
        print("Login failed. Incorrect username or password.")

# 在此调用登录函数
login()
