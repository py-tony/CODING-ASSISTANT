# Compulsory Task 2:
# Request user input of weight and height:
weight = float(input("Enter your Weight (kg): "))
height = float(input("Enter your Height (m): "))
print("")
# print user weight and height in kg and m:
print(f"Your weight is {weight}kg.")
print(f"Your height is  {height}m.")
print("")
# Calculates BMI
bmi = weight / height ** 2
print(f"Your BMI is: {bmi:.2f}")
print("")

# Checks if user is obese, overweight, normal or underweight:
if bmi >= 30:
    print(f"According to your BMI of {bmi:.2f} you are obese.")

elif bmi >= 25:
    print(f"According to your BMI of {bmi:.2f} you are overweight.")

elif bmi >= 18.5:
    print(f"According to your BMI of {bmi:.2f} you are normal.")

elif bmi < 18.5:
    print(f"According to your BMI of {bmi:.2f} you are underweight.")
