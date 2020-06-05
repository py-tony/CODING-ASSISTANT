# Compulsory Task 2:

# Set Variables for Name & Password:
username = " "
password = " "

# Request user input:
# If username & password is less than 4 char. Request user input again.
while username and password != "":
    username = input("Username: ")
    password = input("Password: ")
    username_len = len(username)
    password_len = len(password)

    # Check that Username & Password is more than 4 characters long.
    if username_len < 4 and password_len < 4:
        print("You have entered less than 4 Characters.")
        print("Please make you've entered more than 4 characters for both Username and Password")
    elif username_len > 4 and password_len > 4:
        print(f"Hi {username}.")
        print("")
    # exit(0)

# Logical Error: Infinite Loop.

# exit(0) is needed to end loop.
# exit(0) is missing indentation.
