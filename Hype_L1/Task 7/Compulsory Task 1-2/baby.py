# Compulsory Task 1:

# Request user's birth year:
birth_year = input("Enter your birth year: ")

# Calculates user's age:
age_check = 2020 - int(birth_year)
print(f"You are {age_check} years old. ")

# Informs user's if they're old enough:
if age_check >= 18:
    print("Congratulations you are old enough! ")
else:
    print("You're too young.")
