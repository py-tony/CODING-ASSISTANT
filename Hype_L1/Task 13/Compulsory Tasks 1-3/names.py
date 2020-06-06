# Compulsory Task 2:

i = 0
pupil_names = ""

print("Enter Student Name below.")
print("When done entering student name's type word: \'Stop\'.")
print("")

while pupil_names != 'Stop':
    i += 1
    pupil_names = input("Name: ").capitalize()
i -= 1
print("")
print(f"You have {i} students.")