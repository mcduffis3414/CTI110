# CTI-110
#P2HW2 - GradeBook
# Solomon McDuffie
# 7 April 2023

# add input integer values for the grades

module_one = int(input("Module 1: "))
module_two = int(input("Module 2: "))
module_three = int(input("Module 3: "))
module_four = int(input("Module 4: "))
module_five = int(input("Module 5: "))
module_six = int(input("Module 6: "))

grades = [module_one, module_two, module_three, module_four, module_five, module_six]

# print a results line

print('-------------Results------------')

# calculate the lowest grade

print(f'Lowest grade: {min(grades)}')

# calculate the highest grade

print(f'Highest grade: {max(grades)}')

# calculate the sum of the grades

print(f'Sum of grades: {sum(grades)}')

# calculate the average of the grades

print(f'Average: {sum(grades) / len(grades)}')

print('------------------------------------')

