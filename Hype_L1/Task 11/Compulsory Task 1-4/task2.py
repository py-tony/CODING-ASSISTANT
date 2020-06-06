# Compulsory Task 2:

# Request user input on building shape:
building_shape = input("Enter Building Shape: ").capitalize()
# Check if input matches:
# Run matched input and calculate area:
# For square:
if building_shape == "Square":
    sq_length = float(input("Enter Length of Square: "))
    a_square = sq_length**2
    print(f"Area that will be taken up = {a_square}")
# For Rectangle:
if building_shape == "Rectangle":
    rect_length = float(input("Enter Length of Rectangle: "))
    rect_width = float(input("Enter Width of Rectangle: "))
    a_rect = rect_length * rect_width
    print(f"Area that will be taken up = {a_rect}")
# For Circle:
if building_shape == "Circle":
    import math
    pi = math.pi
    radius = float(input("Enter Radius of Circle: "))
    a_circle = pi * radius ** 2
    print(f"Area that will be taken up = {a_circle:.2f}")

