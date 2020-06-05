# Compulsory Task 2:

# Import Random to generate random list:
import random

# Open text file 1 to write to:
numbers1 = open("numbers1.txt", 'w')

# Generate random list 1:
list_1 = [random.randrange(1, 50, 1)for x in range(0, 10)]
# Write list to text file numbers_1.txt:
numbers1.write(str(list_1))

# Open text file 2 to write to:
numbers2 = open("numbers2.txt", 'w')
# Generate random list 2:
list_2 = [random.randrange(1, 50, 1)for y in range(0, 10)]
# Write list to text file numbers_2.txt:
numbers2.write(str(list_2))

# Close text files:
numbers1.close()
numbers2.close()
# Open text files for read:
numbers1_read = open("numbers1.txt", 'r')
numbers2_read = open("numbers2.txt", 'r')

# Open text file to write:
all_numbers = open("all_numbers.txt", 'w')

# Combine list 1 & list 2:
list_3 = list_1 + list_2
# Sort list:
list_3.sort()
# Write to text file all_numbers:
all_numbers.write(str(list_3))

# Close all text files:
numbers1.close()
numbers2.close()
all_numbers.close()
