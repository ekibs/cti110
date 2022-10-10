# CTI-110
# P2HW2 - List
# Eric Kibler
# 10/10/2022
#
# Pseudocode for Grade List
    # Get test score inputs from user
    # Program calculates sum of users test grades
    # Program divides the sum of the scores by the amount of scores
    # Program displays the lowest grade, the highest grade, the sum of all grades, and the average of the grades
module1 = float(input('Enter grade for Module 1: '))
module2 = float(input('Enter grade for Module 2: '))
module3 = float(input('Enter grade for Module 3: '))
module4 = float(input('Enter grade for Module 4: '))
module5 = float(input('Enter grade for Module 5: '))
module6 = float(input('Enter grade for Module 6: '))
testGrades = [module1, module2, module3, module4, module5, module6]
gradeLength = len(testGrades)
lowestGrade = min(testGrades)
highestGrade = max(testGrades)
gradeSum = sum(testGrades)
gradeAverage = gradeSum / gradeLength 
print()
print('------------Results------------')
print('Lowest Grade:        ', lowestGrade)
print('Highest Grade:       ', highestGrade)
print('Sum of Grades:       ', gradeSum)
print(f'Average:              {gradeAverage:.2f}')
print('---------------------------------------')