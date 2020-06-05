# Compulsory Task 3:

# Set variables:
name = ""
wrong_list = []
# While user input is not 'John':
while name != 'John':
    # Request user name:
    name = input("Name: ").capitalize()
    # If user name is not 'John', add user input name to a list:
    if name != 'John':
        wrong_list.append(name)
    # Print all the user input's of incorrect names in a list:
    print(f"Incorrect Names: {wrong_list}")

# If John, greet John:
print("")
print(f"Hello, {name}.")
