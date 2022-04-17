#CTI-110
#P2HW2 - Score Avg
#Rashad Lawrence
#April 15th, 2022
#

#get all score inputs
score1 = float(input('Enter score #1:'))
score2 = float(input('Enter score #2:'))
score3 = float(input('Enter score #3:'))
score4 = float(input('Enter score #4:'))
score5 = float(input('Enter score #5:'))
score6 = float(input('Enter score #6:'))
score7 = float(input('Enter score #7:'))

#Create the list
score_list = [score1, score2, score3, score4, score5, score6, score7]

#calculate lowest score
lowest = min(score_list)


#drop lowest score
score_list.remove(min(score_list))

#calculate new avg
new_avg = sum(score_list) / 6

#display results
print('----Results-------')
print(f'Lowest Score : [{lowest:.1f}]')
print(f'Modified List :{score_list}')
print(f'Scores Average : {new_avg:.2f}')
print('-------------------')
