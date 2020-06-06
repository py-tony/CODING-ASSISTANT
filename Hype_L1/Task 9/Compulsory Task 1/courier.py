# Compulsory Task 1:

package_price = float(input("Enter Price of Package (Rands): "))

delivery_dist = float(input("Enter Total Delivery Distance (Kilometers): "))
print("")
# How to:

input("To select please type in \"QUOTED OPTION\". Thank you:)\n"
      "Press Enter to continue: ")
print("")
# User Preferences:

# Delivery Options:
delivery_opt1 = "Air"
delivery_opt2 = "Freight"
print("Air = R0.36 p/km\n"
      "Freight = R0.25 p/km")
delivery_options = input("Would you like your package to be delivered via \"Air\" or \"Freight\"?\n"
                         ": ").capitalize()
# Checks user preference:
if delivery_options == delivery_opt1:
    print("Air Price @ R0.36 p/km")
    delivery_price = 0.36
if delivery_options == delivery_opt2:
    print("Freight @ R0.25 p/km")
    delivery_price = 0.25
print("")

# Insurance Options
insurance_opt1 = "Full"
insurance_opt2 = "Limited"
print("Full Insurance = R50.00\n"
      "Limited Insurance = R20.00")
insurance_options = input("Would you like insurance on your package we offer: \"Full\" or \"Limited\"\n"
                          ": ").capitalize()
# Checks user preference:
if insurance_options == insurance_opt1:
    print("Your Package will be Fully Insured.")
    insurance_price = 50.00
if insurance_options == insurance_opt2:
    print("Your Package will be Insured.")
    insurance_price = 25.00
print("")

# Gift Options:
gift_opt1 = "Yes"
gift_opt2 = "No"
print("Gift = R15.00\n"
      "No Gift = R0.00")
gift_options = input("Is this a Gift? (Yes or No): ").capitalize()
# Checks User Preference:
if gift_options == gift_opt1:
    print("Your Package will be sent as a Gift.")
    gift_price = 15.00
if gift_options == gift_opt2:
    print("Your Package will not be sent as a Gift.")
    gift_price = 0
print("")

# Priority Options
priority_opt1 = "Priority"
priority_opt2 = "Standard"
print("Priority Shipping = R100.00\n"
      "Standard Shipping = R20.00")
priority_options = input("Would you like \"Priority\" Shipping or \"Standard Shipping\"?\n"
                         ": ").capitalize()
# Checks user preference:
if priority_options == priority_opt1:
    print("Your Package will has Full Priority.")
    priority_price = 100.00
if priority_options == priority_opt2:
    print("Your Package has Standard Priority.")
    priority_price = 20.00
print("")

# Calculates Delivery Price:
total_delivery = delivery_dist * float(delivery_price)
print(f"Total Delivery Price: R{total_delivery:.2f}")
print("")

# Calculates Preference:
total_pref = insurance_price + gift_price + priority_price
print(f"Total Preference Price: R{total_pref:.2f}")
print("")

# Calculates Total Price:
total_price = package_price + total_delivery + total_pref
print(f"Your Total: R{total_price:.2f}")