# Compulsory Task 2:

# Calculates Total Price for hotel stay:
def hotel_cost(num_nights):
    price_p_night = 100
    hotel_total = price_p_night * num_nights

    return hotel_total


# Calculates Plane Ticket costs:
def plane_cost(destination):
    # Destination flight prices
    flight_prices = {
        1: 600,  # Boston
        2: 620,  # Chicago
        3: 750,  # New York
        4: 800,  # Los Angeles
        5: 850  # Philadelphia
    }
    # Check user destination choice and return price:
    if destination == 1:
        return flight_prices[1]
    elif destination == 2:
        return flight_prices[2]
    elif destination == 3:
        return flight_prices[3]
    elif destination == 4:
        return flight_prices[4]
    elif destination == 5:
        return flight_prices[5]
    else:
        print(f"Invalid Input: {destination}. Enter a number from (1 - 5).")
        return exit(0)


# Calculates Total Price for car rental:
def car_rental(rental_days):
    rental_price = 25
    total_rental = rental_price * rental_days
    return total_rental


# Calculates Total Price for Holiday:
def holiday_cost():
    holiday_total = hotel_cost(nights) + plane_cost(flight_choice) + car_rental(rental_period)
    return holiday_total


# Hotel Costs:
print("Hotel Costs:")
# Request user input of nights staying in hotel:
nights = int(input("How many nights will you be staying?\n"
                   ": "))
print(f"For {nights} Nights:    ${hotel_cost(nights):.2f}")  # Total Price for hotel stay:
print("")

# Plane Costs:
# Flight options for user to see:
flight_options = (
    "1: Boston \n"
    "2: Chicago \n"
    "3: New York \n"
    "4: Los Angeles \n"
    "5: Philadelphia"
)
print("Plane Costs:")
print("Which city will would you like to fly to?")
print(flight_options)
# Request user input of destination:
flight_choice = int(input("Enter a number (1 - 5)\n"
                          ": "))
print(f"Plane Ticket:   ${plane_cost(flight_choice):.2f}")  # Total Price for flight:
print("")

# Car Rentals:
print("Car Rentals:")
# request user input of car rental period:
rental_period = int(input("How many days will you be renting the car?\n"
                          ": "))
print(f"For {rental_period} Days:  ${car_rental(rental_period):.2f}")  # Total Price for car rental:
print("")

# Holiday Costs:
print("Holiday Costs:")
print(f"For {nights} Nights:    ${hotel_cost(nights):.2f}")  # Total Price for hotel stay:
print(f"Plane Ticket:   ${plane_cost(flight_choice):.2f}")  # Total Price for flight:
print(f"For {rental_period} Days:   ${car_rental(rental_period):.2f}")  # Total Price for car rental:
print("")
print(f"Holiday Total Price:    ${holiday_cost():.2f}")  # Total Price:
print("Hope you enjoy your Holiday :)")
