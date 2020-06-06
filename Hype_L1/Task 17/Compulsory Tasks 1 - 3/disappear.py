# Compulsory Task 3:

# Request user's string:
user_string = input("Enter sentence: ").lower()

# Requests user's input on which characters to remove from string:
user_remove = input("Enter characters you'd like to remove from string: ").lower()

# Removes ',' if user's input contains ','
user_remove = user_remove.replace(",", "")

# Make a copy of user's string:
new_string = user_string

# Check character in user input of characters to remove:
# Replace character with ""(nothing):
for char in user_remove:
    new_string = new_string.replace(char, "")

# Print user string with removed characters:
print(new_string)
