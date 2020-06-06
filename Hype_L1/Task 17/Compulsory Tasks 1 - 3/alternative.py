# Compulsory Task 1:

# Regardless of spaces in between words the next word will always start with .upper()

# Request user input of string:
string = input("Enter a string: ")

# Declare variable for alternative string case.
new_string = ""

# Make i = True:
i = 1
# Check character in string.
for char in string:
    # Make Char Capital case:
    if i:
        new_string += char.upper()
    # Make Char Lower case:
    else:
        new_string += char.lower()

# Regardless of whitespaces in between words. Next word will star with uppercase.
    # Make following letter after whitespace start with uppercase:
    if char == ' ':
        i = True
    # Make next letter lowercase if previous is uppercase:
    elif char != '':
        i = not i

# Print alternative case string:
print(new_string)
