# Compulsory Task 1:

# Function: Prints days of the week:
def days_of_week():
    return '| Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |'


# Function: Replaces every second word in a sentence with 'Hello':
def replace_hello(x):
    # Convert string into list:
    sent_list = x.split(" ")
    # Set variable for empty list to add items/ words to:
    new_list = []
    # Index start position of 0:
    i = 0

    # For index in sentence_list:
    for index in sent_list:
        # Check index modulus 2 is = 0, YES, append that item to new list:
        if i % 2 == 0:
            new_list.append(index)
            # Add one to index to go to next index.
            i += 1
        # NO, append word 'Hello':
        else:
            new_list.append('Hello')
            # Add one to index to go to next index.
            i += 1

    # Set variable with empty string:
    string = " "
    # Covert list to string:
    return string.join(new_list)


# Call 'days of week'function. Print days of the week:
print(days_of_week())

print("")
# Call 'replace_hello' function. Print string with replaced words:
user_string = input("Enter a string: ")
print(replace_hello(user_string))
