# CTI-110
# P4HW2 - Salary Calculator
# Solomon McDuffie
# 30 April 2023

# Enter the employees name or terminate the program
employee = input("Enter employee's name or 'Done' to terminate: ")

employee_num = 1
overtime_total = 0
regular_pay = 0
gross_total = 0

# Ask for employee informaton
while employee != 'Done':
            
    hours = float(input("How many hours did {} work? ".format(employee)))

    pay_rate = float(input("What is {} pay rate? ".format(employee)))

    overtime = hours - 40

    overtime_pay = (overtime * pay_rate)

    reg_total = (hours - overtime) * pay_rate

# Gross pay definition
    gross_pay = regular_pay + overtime_pay


# Is this overtime hours or not.
    if hours > 40:
        overtime
    else:
        overtime = 0
    
# Will they recieve overtime pay?
    if overtime > 0:
        overtime_pay
        overtime_total += overtime_pay
        
    else:
        overtime_pay = 0
        overtime_total = overtime_total
    
# Regular pay for everyone, calculating only hours worked under 40
    if hours > 40:
        regular_pay
        reg_total += regular_pay
    else:
        regular_pay = pay_rate * hours
        reg_total += regular_pay

# Loop statement to calculate gross pay
    if hours > 40:
        gross_pay
        gross_total += gross_pay
    else:
        gross_pay = hours * pay_rate
        gross_total += gross_pay
        

# White space
    print()

# Name of employee for report
    print("Employee Name:  ", employee)

# White space is important
    print(' ')
 
# Report information
    print("Hours Worked", "  ", "Pay Rate", "  ", "OverTime", "  ", "OverTime Pay", "  ", "RegHour Pay", "   ", "Gross Pay")

# Line
    print("---------------------------------------------------------------------------------------")

# Output calculations
    print ('{:<13.2f}'.format(hours), '{:^8.2f}'.format(pay_rate), '{:^14.2f}'.format(overtime), '{:^10.2f}'.format(overtime_pay), '{:^21.2f}'.format(regular_pay), '{:^8.2f}'.format(gross_pay))

# White space 
    print()

# Name again
    employee = input("Enter employee's name or 'Done' to terminate: ")

# Calculate the total of employees time entered
    employee_num += 1
    

else:
    # Calculations
    print('Total number of employees entered:{}'.format(employee_num - 1))
    print('Total amount payed for overtime: ${:.2f}'.format(overtime_total))
    print('Total amount payed for regular hours: ${:.2f}'.format(reg_total))
    print('Total amount payed in gross: ${:.2f}'.format(gross_total))
