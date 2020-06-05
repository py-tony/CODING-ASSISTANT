# Compulsory Task 2:

# Request user input for start year:
year_start = int(input("What year do you want to start with?\n"
                       ": "))
# Request user input for how many years to check:
year_check = int(input("How many years do you want to check?\n"
                       ": "))

# Check if leap year or not leap year:
for i in range(0, year_check):

    if year_start % 4 != 0:
        print(f"{year_start}\t is not leap year")
        year_start += 1

    elif year_start % 4 == 0:
        print(f"{year_start}\t is leap year")
        year_start += 1
