# Compulsory Task 2:

# Request user's 3 items:
print("Enter 3 Products Below.")
item1 = input("Enter Product 1: ")
item2 = input("Enter Product 2: ")
item3 = input("Enter Product 3: ")
print("")
# Request price of the 3 items:
print("Enter Price of Each Product.")
price1 = float(input("Enter Price of Product 1: "))
price2 = float(input("Enter Price of Product 2: "))
price3 = float(input("Enter Price of Product 3: "))
print("")
# print item and price:
print("List and Prices:")
print(f"{item1.capitalize()}:\t{price1:.2f}")
print(f"{item2.capitalize()}:\t{price2:.2f}")
print(f"{item3.capitalize()}:\t{price3:.2f}")
print("")
# Calculates total price:
total_price = price1 + price2 + price3
# Calculates average price:
avg_price = total_price / 3

# Prints total and average price for user:
print(f"The Total of {item1}, {item2}, {item3} is R{total_price:.2f} "
      f"and the average price of the items are R{avg_price:.2f}.")

