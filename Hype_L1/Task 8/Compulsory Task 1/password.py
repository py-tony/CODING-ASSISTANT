# Compulsory Task 1:

# Request user to enter password:
password = input("Password: ")

have_length = False
up_case = False
low_case = False
have_num = False
num_questions = 0
# Check if password is 6 char or more:
have_length_check = input("Does your password have 6 or more characters? (YES/NO): ").capitalize()
if have_length_check == 'Yes':
    have_length = True
    num_questions += 1
# Check if password has a Capital case char:
up_case_check = input("Does your password have a CAPITAL CASE character? (YES/NO): ").capitalize()
if up_case_check == 'Yes':
    up_case = True
    num_questions += 1
# Check if password has lower case char:
low_case_check = input("Does your password have a lower case character? (YES/NO): ").capitalize()
if low_case_check == 'Yes':
    low_case = True
    num_questions += 1
# Check if password has number char:
have_num_check = input("Does your password have a number characters? (YES/NO): ").capitalize()
if have_num_check == 'Yes':
    have_num = True
    num_questions += 1
# Checks returned results. Is password suitable:
print("")
if num_questions >= 3:
    print("Password is suitable.")
# if not check again:
if num_questions <= 2:
    print("Your password does not match requirements.\n"
          "Make sure your password has:\n"
          "6 or more characters.\n"
          "A Capital case character.\n"
          "A lower case character.\n"
          "A number character.\n")
