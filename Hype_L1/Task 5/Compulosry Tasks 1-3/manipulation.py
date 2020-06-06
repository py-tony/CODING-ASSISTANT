# Compulsory Task 3:

# Request user's sentence:
str_manip = input("Enter a sentence: ")

# Calculates user's input character length:
str_len = len(str_manip)
print(str_len)

# Replaces last letter in user's input with @ character:
last_char = str_manip[-1::]
str_edit = str_manip.replace(last_char, "@")
print(str_edit)

# Collects last 3 characters in user's input and reverses it:
last_3 = str_manip[-1:-4:-1]
print(last_3)

# Creates 5 char word using first 3 char in first word and last 2 char in last word:
new_word_first = str_manip[0:3:1]
new_word_last = str_manip[-1:-3:-1]
print(new_word_first + new_word_last[::-1])
