# Compulsory Task 4:

# Request user input of integer
integer = int(input("Enter an Integer: "))

# Check if integer is divisible by both 2 and 5:
if integer % 2 == 0 and integer % 5 == 0:
    print("Is divisible by 2 and 5")
# Check if integer is divisible by 2 or 5:
elif integer % 2 == 0 or integer % 5 == 0:
    print("Is divisible by 2 or 5.")
# Check if integer is not divisible by 2 or 5:
elif integer % 2 != 0 or integer % 5 != 0:
    print("Is not divisible by 2 nor 5.")
