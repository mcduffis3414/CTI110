# CTI-110
# P3HW2 - Salary
# Solomon McDuffie
# 23 April 2023

# variables for information

name = input("Please enter employee name: ")
hours = float(input("Please enter the number of hours the employee worked this week: "))
pay_rate = float(input("Please enter the pay rate of the employee: "))
overtime_pay = float(input("Please enter the rate of overtime pay: "))
overtime = (hours - 40)
regular_pay = (pay_rate * hours)
overtime_earnings = (overtime_pay * overtime)


# is this overtime or not?

if hours > 40:
    print(name, "worked overtime this week.")
if hours < 40:
    print(name, "worked less than full time.")
if hours == 40:
    print(name, "worked their regular hours.")

# let's calculate the total pay

if overtime != 0:
    total_pay = (pay_rate * hours) + (overtime_pay * overtime) 

elif overtime == False:
    total_pay = regular_pay

# outputs

print("----------------------------------")
print("Employee's name:", name)
print("Hours Worked    Pay Rate    OverTime Pay    RegHour Pay    Gross Pay")
print("--------------------------------------------------------------------")
print(f'{hours:<16.2f}{pay_rate:<12.2f}{overtime_earnings:<16.2f}{regular_pay:<15.2f}{total_pay:<11.2f}')
