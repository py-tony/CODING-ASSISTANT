import random

number = random.randint(1, 11)

while number != 5:
    number = random.randint(1, 11)
    print(number)

    if number == 5:
        exit(0)
