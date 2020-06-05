# Compulsory Task 3:

# Sample String:
string = 'google.com'

# Set variable for dictionary:
occurrences = {}

# For each char in string:
for char in string:
    # Check if char occurs more then once if so add 1 to each occurrence:
    if char in occurrences:
        occurrences[char] += 1
    # Check if char occurs more than once if not add 1:
    else:
        occurrences[char] = 1

# Print occurrence dictionary:
print(occurrences)
