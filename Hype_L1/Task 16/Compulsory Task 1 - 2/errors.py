# This example program is meant to demonstrate errors.

# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

# Compulsory Task 1:

# Syntax Error: Missing Parentheses:
print("Welcome to the error program")
# Syntax Error: Missing Parentheses
# Syntax Error: Unexpected Indentation:
print("\n")

# Syntax Error: Unexpected Indentation:
# Statement has no effect. "ageStr == "24 years old""    # I'm 24 years old.
# Syntax Error: Repetition of words "years old"
age = "24"
print("I'm " + age + " years old.")

# Syntax Error: Can't do maths with strings only integers:
three = 3
# Syntax Error: Unexpected Indentation:
# : Type casting from string to integer:
answerYears = int(age) + three

# Syntax Error: Missing Parentheses
# Syntax Error: Unexpected " " around answerYears
# : Can't concatenate strings with integers only strings with strings:
print("The total number of years: " + str(answerYears))

# Syntax Error: Missing Variable:
# Runtime Error: Missing variable,
answerMonths = answerYears * 12

# Missing Variable of 6 months:
# Add 6 months to
sixthMonth = 6

# Logical Error: 324 months old, should be 330 months old:
# Formatted String:
print(f"In 3 years and 6 months, I'll be {answerMonths + sixthMonth} months old.")

# HINT, 330 months is the correct answer
