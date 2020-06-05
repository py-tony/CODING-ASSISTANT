# This example program is meant to demonstrate errors.

# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

# Compulsory Task 1:

name = "Tim"

# Syntax Error: Unexpected Indentation:
surname = " Jones"
age = 21

# Syntax Error: Missing Quotation Mars around word - is:
# Syntax Error: Can't concatenate strings with integers:
# : Type conversion to strings.
fullMessage = name + surname + " is " + str(age) + " years old."

# Syntax Error: Missing Parentheses:
print(fullMessage)
