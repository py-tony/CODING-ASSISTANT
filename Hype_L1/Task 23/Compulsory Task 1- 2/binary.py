# Compulsory Task 1:

# Import math to run math functions::
import math

# Request user input of binary number:
binary_num = list(input("Binary Number: "))

# Set variable, value to 0:
value = 0

# Loop each bit in range of binary numbers:
for bit in range(len(binary_num)):
    # Remove bit and return last:
    number = binary_num.pop()
    # Check if number is equal to 1:
    if number == '1':
        # Calculate binary to decimal:
        value = value + math.pow(2, bit)

# Print Decimal Value:
print(f"Decimal Value: {value:.0f}")
