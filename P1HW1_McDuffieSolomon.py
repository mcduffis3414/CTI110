# travel expenses calculator
# 6 April 2023
# CTI-110 P1HW1 - Travel Expense
# Solomon McDuffie

print("This program calculates and displays your travel expenses")

# varible should equal an input from the user, the numbers will be prescribed an integer string.

budget = int(input("Enter your budget: "))

destination = input("What is your destination: ")

gas = int(input("How much will you spend on gas: "))

hotel = int(input("How much will you spend on hotel accomodations: "))

food = int(input("How much will you spend on food: "))

# now that all the variables are defined, restate everything and do math.

print("--------------Can you afford this trip?---------------")

print("Destination: ", destination)

print("Budget: ", budget)

print("Gas", gas)

print("Hotel", hotel)

print("Food", food)

# Start with the budget and subtract the intergers values of expenses

remaining_balance = int(budget - gas - hotel - food)

print("remaining balance: ", remaining_balance)

