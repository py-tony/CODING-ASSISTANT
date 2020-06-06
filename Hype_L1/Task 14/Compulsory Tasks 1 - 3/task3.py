# Compulsory Task 3:

import math

# Prints 20 - 1:
i = 20
while i > -1:
    print(i)
    i -= 1  # Subtracts 1 from i in loop to count backwards.
print("")

# Finds even numbers from 1 - 20
for x in range(1, 21):
    if x % 2 == 0:
        print(x)
print("")

# Prints '*' from 1* to 6*'s:
star = "*"
multiply = 0
for star in range(1, 6):
    print(star * "*")
    star *= 1   # Multiplies star in every loop to add *.
print("")

# Explains how to use program:
print("Enter Two Positive Integers Below.")

# Request user input of positive integers:
pos_int_1 = int(input("Enter Integer 1: "))
pos_int_2 = int(input("Enter Integer 2: "))

print("")
# Prints out Common Divisors of Positive Integer 1:
print(f"Divisors of {pos_int_1}:")
for y_1 in range(1, pos_int_1 + 1):
    answer1 = pos_int_1 / y_1

    if pos_int_1 % y_1 == 0:
        print(f"{pos_int_1} / {y_1} = {answer1}")

print("")
# Prints out Common Divisors of Positive Integer 2:
print(f"Divisors of {pos_int_2}:")

for y_2 in range(1, pos_int_2 + 1):
    answer2 = pos_int_2 / y_2

    if pos_int_2 % y_2 == 0:
        print(f"{pos_int_2} / {y_2} = {answer2} ")

print("")

# Calculates Greatest Common Divisor (GCD):
if pos_int_1 % y_1 == 0 and pos_int_2 % y_2 == 0:
    gcd = math.gcd(pos_int_1, pos_int_2)
    print(f"The GCD of {pos_int_1} & {pos_int_2} is: {gcd}")
