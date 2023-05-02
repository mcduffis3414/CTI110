# Travel expenses calculator
# 7 April 2023
# P2HW1 - Travel
# Solomon McDuffie

print("This program calculates and displays your travel expenses")

# varible should equal an input from the user, the numbers will be prescribed an integer string.

budget = float(input("Enter your budget: "))

destination = input("What is your destination: ")

gas = float(input("How much will you spend on gas: "))

hotel = float(input("How much will you spend on hotel accomodations: "))

food = float(input("How much will you spend on food: "))

# now that all the variables are defined, restate everything and do math.

print("--------------Can you afford this trip?---------------")

print("Destination: ", destination)

print("Budget: ", budget)

print("Gas: ", gas)

print("Hotel: ", hotel)

print("Food: ", food)

# Start with the budget and subtract the intergers values of expenses

remaining_balance = float(budget - gas - hotel - food)

print("remaining balance: ", remaining_balance)

