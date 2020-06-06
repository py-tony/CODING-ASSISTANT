# Compulsory Task 1:

# Request user input for integer:
y = int(input("Enter Number: "))

print(f"The {y} times table is:")
# Multiplies user input from 1 to 10:
for x in range(1, 13):
    answer = x * y
    print(f"{x} x {y} = {answer}")
