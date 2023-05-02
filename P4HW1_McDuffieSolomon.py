# CTI-110
# P4HW1 - Score List
# Solomon McDuffie
# 30 April 2023
#
num_scores = int(input('How many scores do you want to enter? '))
print()
i = 1
score_list = []


while i <= num_scores:
    print('Enter score #{}: '.format(i), end= '')
    score = float(input())
    
    if score < 0 or score > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")

    else:
        score_list.append(score)
        i+=1

# Get the min score out of my total score list

lowest_score = min(score_list)
score_list.remove(lowest_score)
score_avg = sum(score_list)/len(score_list)

# Equate letter grades to averages (90s are A's, 80s are B's, etc)

if score_avg >= 90:
    grade = 'A'

elif score_avg >= 80:
    grade = 'B'

elif score_avg >= 70:
    grade = 'C'

else:
    grade = 'F'

print("\n")

print('--------------Results-----------')
print('Lowest Score:',lowest_score)
print('Modified List:', score_list)
print('Scores Average:', f'{score_avg:.2f}')
print('Grade:', grade)



    
