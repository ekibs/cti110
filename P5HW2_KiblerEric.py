# This program utilizes functions to create a math quiz game
    # 11/25/2022
    # CTI-110 P5HW2 - Math Quiz
    # Eric Kibler
    #Pseudocode:
        #Create the main menu that uses function calls inside a loop to start the math game the user requests, or quits.
        #For each function, assign two random numbers and have the user input the solution to the numbers' equation.
        #If the user is correct, display a congratulatory message along with how many attempts it took. 
        #Otherwise, tell the user their answer is either too low or high and have them guess again.
        #
import random
def addition():
    attempt = 1
    num1 = random.randint(100, 500)
    num2 = random.randint(100, 500)
    sum = (num1 + num2)
    print('Solve this equation:')
    print(' ', num1)
    print('+', num2)
    answer = int(input('Type answer here...'))
    while answer != sum:
        if answer > sum:
            print('Your answer is too high.')
        else:
            print('Your answer is too low.')
        attempt += 1
        answer = int(input('Try again: '))
    if answer == sum:
        print('Congratulations! Your answer is correct!')
        print('Attempts: ', attempt)
def subtraction():
    attempt = 1
    num1 = random.randint(100, 500)
    num2 = random.randint(100, 500)
    difference = (num1 - num2)
    print('Solve this equation:')
    print(' ', num1)
    print('-', num2)
    answer = int(input('Type answer here...'))
    while answer != difference:
        if answer > difference:
            print('Your answer is too high.')
        else:
            print('Your answer is too low.')
        attempt += 1
        answer = int(input('Try again: '))
    if answer == difference:
        print('Congratulations! Your answer is correct!')
        print('Attempts: ', attempt)
choice = 0
while choice != 3:
    print('\nMAIN MENU')
    print('---------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    choice = int(input('\nPlease choose one of the menu options: '))
    if choice == 1:
        addition()
    elif choice == 2:
        subtraction()
    elif choice == 3:
        print('Thank you for playing. Goodbye.')
    else:
        print('\nError! Please enter a number 1-3.')