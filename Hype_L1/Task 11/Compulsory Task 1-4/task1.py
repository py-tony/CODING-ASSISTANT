# Compulsory Task 1:

num1 = 10
num2 = 20
num3 = 30

# Greater than value:
if num1 > num2:
    print(f"{num1} is Greater than {num2}.")

else:
    print(f"{num2} is Greater than {num1}.")

# Odd or Even check:
if (num1 % 2) == 0:
    print(f"{num1} is an Even Number.")

else:
    print(f"{num1} is an Odd Number.")

# Print list from largest to smallest.
print("Numbers Sorted From Largest to Smallest:")
num_list = [num1, num2, num3]
num_list.sort(reverse=True)
print(num_list)