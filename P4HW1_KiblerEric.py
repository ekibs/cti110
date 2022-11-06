# CTI-110
# P4HW1 - Score List
# Eric Kibler
# 11/6/2022
#Pseudocode
    # Get input for amount of scores user wants to enter
    # initialize counter variables 
    # declare list variable for scores
    # create a loop asking the user to input 'x' amount of scores
    # create an if-else loop to only allow scores between 0 and 100
    # initialize variables to calculate grade results for score list
    # display results 
scoreAmount = int(input('How many scores do you want to enter? '))
loopCounter = 0
i = 1
scores = []
print()
while loopCounter < scoreAmount:
    score = int(input('Enter score #'+str(i)+': '))
    if (score < 0 or score > 100):
        print('\nInvalid score!')
        print('Score should be between 0 and 100.')     
    else:
        scores.append(float(score))
        i+=1
        loopCounter+=1

scores.sort()
lowestScore = scores[0]
scores.remove(lowestScore)
scoreAvg = sum(scores) / len(scores)

if scoreAvg >= 90:
    grade = 'A'
elif scoreAvg >= 80:
    grade = 'B'
elif scoreAvg >= 70:
    grade = 'C'
elif scoreAvg >= 60:
    grade = 'D'
else:
    grade = 'F'
print()
print()
print('------------Results------------')
print('Lowest Score  :', lowestScore)
print('Modified List :', scores)
print(f'Scores Average: {scoreAvg:.2f}')
print('Grade         :', grade)
print('---------------------------------------')


