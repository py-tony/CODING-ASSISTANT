# Compulsory Task 1:

# Open DOB.txt file:
users_list = open('DOB.txt', 'r', encoding='utf-8-sig')

# Set variables for names & dates:
names = ""
dates = ""

# Loop through lines in file:
for line in users_list:
    # Make line array/list:
    user = line.split(" ")

    # Grab items in array to print initial and surname:
    names += f"     {user[0][0]} {user[1]}\n \n"

    # Grab items in array to print day, month, and year:
    dates += f"     {user[2]} {user[3]} {user[4]}\n"

# Print Names from DOB.txt:
print("Names:")
print("")
print(names)

# Print Date of Births from DOB.txt:
print("Date of Birth:")
print("")
print(dates)

# Close DOB.txt file:
users_list.close()
