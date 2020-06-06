# Compulsory Task 3:

number = ''
i = 0
total = 0
while number != "-1":
    number = input("Enter a number: ")
    i += 1
    total += int(number)
print("")

i -= 1
total += 1
print(f"Total Entries = {i}")
print(f"Total Sum = {total}")
print("")

average = total / int(i)
print(f"Average = {average}")
