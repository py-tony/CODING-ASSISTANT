# Compulsory Task 1:
# Open/ Create text file to write to:
reg_form = open("reg_form.txt", 'w')

# Write heading to text file:
reg_form.write("Student ID Numbers: \n")
reg_form.write("\n")

# Request for number of registrations:
number = int(input("Number of students registering: "))

# Loop for number of registrations:
for i in range(1, number + 1):
    # Request student ID Number:
    id_no = input("ID Number: ")
    # Print ID Number to text file:
    reg_form.write(f"{id_no} \n")

# Close text file:
reg_form.close()
