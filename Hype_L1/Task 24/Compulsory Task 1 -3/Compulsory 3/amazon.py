# Compulsory Task 3:

# Read from file input.txt:
input_text = open("input.txt", 'r', encoding='utf-8-sig')
# Write to output.txt:
output_text = open("output.txt", 'w')

# Set empty list:
line_list = []

# For each line in text file:
for line in input_text:
    line = line.strip().split(':')
    line = line[:].pop(1)
    line_list.append(line.split(','))  # min, max, avg


# Function: Calculate min:
def min_calc(x):
    y = min(x)

    return y


# Function: Calculate max:
def max_calc(x):
    y = max(x)

    return y


# Function: Calculate avg:
def avg_calc(x):
    y = sum(x) / len(x)

    return y


# Convert string to int list:
list_min = [int(item) for item in line_list[0]]  # Min: List
output_text.write(f"The min of {list_min} is {min_calc(list_min)}.\n")  # Write to output.txt:
# Convert string to int list:
list_max = [int(item) for item in line_list[1]]  # Max: List
output_text.write(f"The max of {list_max} is {max_calc(list_max)}.\n")  # Write to output.txt:
# Convert string to int list:
list_avg = [int(item) for item in line_list[2]]  # Avg: List
output_text.write(f"The avg of {list_avg} is {avg_calc(list_avg)}.\n")   # Write to output.txt:

# Close opened text, files:
input_text.close()
output_text.close()
