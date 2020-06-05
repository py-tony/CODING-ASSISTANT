# Compulsory Task 1:

# Cafe Menu:
menu = ['coffee', 'soft drink', 'salad', 'cake']

# Stock items:
stock = {'coffee': 10,
         'soft drink': 20,
         'salad': 50,
         'cake': 10}
# Price of 1 item in stock:
price = {'coffee': 25.00,
         'soft drink': 15.00,
         'salad': 30.00,
         'cake': 80.00}

# Sum total of stock price:
total = sum(stock[i] * price[i] for i in price)
print(f"Stock Total Price: R{total:.2f}")