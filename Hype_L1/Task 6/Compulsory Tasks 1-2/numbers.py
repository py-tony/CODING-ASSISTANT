# Compulsory Task 1:

# Request user's input of 3 different integers:
print("Enter 3 Different Integers: ")
num1 = int(input("Enter Integer 1: "))
num2 = int(input("Enter Integer 2: "))
num3 = int(input("Enter Integer 3: "))

# The sum of all number:
print("The sum of all the numbers")
sum_addition = num1 + num2 + num3
print(f"{num1} + {num2} + {num3} = {sum_addition}")

# The first number less second number:
print("The first number minus the second number")
sum_subtract = num1 - num2
print(f"{num1} - {num2} = {sum_subtract}")

# The first number multiplied by the last number:
print("The third number multiplied by the first number")
multiply = num3 * num1
print(f"{num3} x {num1} = {multiply}")

# The sum of all 3 numbers divided by the last number:
print("The sum of all three numbers divided by the third number")
sum_divide = (num1 + num2 + num3) / num3
print(f"({num1} + {num2} + {num3}) / {num3} = {sum_divide}")
