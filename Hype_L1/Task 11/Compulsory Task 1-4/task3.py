# Compulsory Task 3:

# Request athlete finish time for all 3 events:
time_swim = float(input("Enter Finish Time For Swimming (min): "))
time_cycle = float(input("Enter Finish Time For Cycling (min): "))
time_run = float(input("Enter Finish Time For Running (min): "))
fin_total = time_swim + time_cycle + time_run
print("")

# Prints total time it took to finish triathlon:
print(f"Total Time {fin_total:.2f} minutes")
print("")

# Checks if athlete receives an award:
# Provincial Colours:
if fin_total <= 100:
    print(f"Congratulations on finishing the race.\n"
          f"Your time of {fin_total:.2f} got you Provincial Colours.")
# Provincial Half Colours:
elif fin_total <= 105:
    print(f"Congratulations on finishing the race.\n"
          f"Your time of {fin_total:.2f} got you Provincial Half Colours.")
# Provincial Scroll:
elif fin_total < 110:
    print(f"Congratulations on finishing the race.\n"
          f"Your time of {fin_total:.2f} got you a Provincial Scroll.")
# No Award:
else:
    print(f"Congratulations on finishing the race.\n"
          f"Your time of {fin_total:.2f} got you No Award.")