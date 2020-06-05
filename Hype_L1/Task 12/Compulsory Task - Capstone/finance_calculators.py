import math
# options
print("Choose either \'investment\' or \'bond\' from the menu below to proceed:")

print("Investment   - To Calculate the amount of interest you'll earn on interest.")
print("Bond         - To Calculate the amount you'll have to pay on a home loan.")
print("")

# Request user option on what to calculate:
menu_choice = input('Calculate \'Investment\' or \'Bond\': ').capitalize()

# Investment Calculations:
if menu_choice == "Investment":
    print("Investment Option: ")
    print("")
    deposit = float(input("Deposit Amount: "))
    i_rate = float(input("Interest Rate: "))
    years = int(input("Number of Years: "))

    # Request if user would like Simple or Compound Interest:
    print("Would you like to invest in \'simple\' or \'compound\' interest:")
    option_choice = input("Enter Option: ").capitalize()

    # Calculates Simple Interest:
    if option_choice == "Simple":
        total_s = deposit * (1 + i_rate / 100 * years)
        print("")
        print(f"R{total_s:.2f}")

    # Calculates Compound Interest:
    elif option_choice == "Compound":
        total_c = deposit * math.pow((1 + i_rate / 100), years)
        print("")
        print(f"R{total_c:.2f}")

    else:
        print("You have entered an invalid option.\n"
              "Please Enter the word \'Simple\' or \'Compound\'.")
# Bond Calculations:
elif menu_choice == "Bond":
    print("Bond Option: ")
    house_value = float(input("House Value: "))
    i_rate = float(input("Interest Rate: "))
    months = int(input("Months: "))
    repayment = house_value * ((i_rate / 100 / 12 * (1 + i_rate / 100 / 12) ** months) / (((1 + i_rate / 100 / 12)
                                                                                           ** months) - 1))
    print("")
    print(f"R{repayment:.2f} pm for {months} months")

else:
    print("You have entered an invalid option.\n"
          "Please Enter \'Investment\' or \'Bond\'.")
