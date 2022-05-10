# CTI-110
# P4HW1 - Score List
# Rashad Lawrence
# 5-9-2022
#


score_size= int(input("How many scores do you want to enter?"))

scores_list = [ ]

for i in range(1, score_size+1):
   print(f'Enter score #:', i)
   score = int(input())
   if (score < 0) or (score > 100):
       print("INVALID Score entered!!!!")
       print("Score should be between 0 and 100")
       print(f'Enter score #', i, "again:")
       score = int(input())
   scores_list.append(score)


lowest =min(scores_list)

scores_list.remove(min(scores_list))

new_avg = sum(scores_list) / score_size
    
if new_avg >= 90:
    grade = 'A'
    
elif new_avg >= 80:
    grade = 'B'
    
elif new_avg >= 70:
    grade = 'C'
    
elif new_avg >= 60:
    grade= 'D'
    
else:
    grade = 'f'


print('----Results-------')
print(f'Lowest Score : [{lowest:.1f}]')
print(f'Modified List :{scores_list}')
print(f'Scores Average : {new_avg:.2f}')
print(f'Grade        :{grade}')
print('-------------------')

