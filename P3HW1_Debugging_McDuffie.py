# P3HW1
# McDuffie, Solomon


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

print("-----------Results-----------")

lowest_grade = min(grades)
print(f"Lowest Grade: ", lowest_grade)
highest_grade = max(grades)
print(f"Highest Grade: ", highest_grade)
sum_grades = sum(grades)
print(f"Sum of Grades: ", sum_grades)
average_grades = (sum_grades)/(len(grades))
print(f"Average: ", average_grades)

print("----------------------------")

# determine letter grade for average

if average_grades >= 90:
    print('Your grade is: A')

if average_grades <= 89:
    print('Your grade is: B')

if average_grades <= 79:
    print('Your grade is: C')

if average_grades <= 69:
    print('Your grade is: F')





