# Travel Expense Calculator
# 09/15/2022
# CTI-110 P1HW2 - Travel Expense
# Eric Kibler
#
print('This program calculates and displays travel expenses.\n')
userBudget = int(input('Enter Budget: '))
userDest = input('Enter your travel destination: ')
userGas = int(input('How much do you think you will spend on gas? '))
userHotel = int(input('Approximately, how much will you need for accomodation/hotel? '))
userFood = int(input('Last, how much do you need for food? '))
expenseSum = userGas + userHotel + userFood
print('------------Travel Expenses------------')
print('Location:', userDest)
print('Initial Budget:', userBudget)
print('Fuel:', userGas)
print('Accomodation:', userHotel)
print('Food:', userFood)
print('Total cost:', expenseSum)
print('Remaining Balance:', userBudget - expenseSum)
# Pseudocode for Travel Expense
    #Display "This program calculates and displays travel expenses"
    #Display "Enter budget"
    #user inputs integer for budget
    #Display "Enter your travel destination"
    #user inputs destination string
    #Display "How much do you think you will spend on gas?"
    #user enters integer amount
    #Display "Approximately, how much will you need for accomodation/hotel?"
    #user inputs integer for hotel cost
    #Display "Last, how much do you need for food?"
    #user inputs integer cost for food
    #insert a variable for the sum of all expenses
    #Display "------------Travel Expenses--------------"
    #Display "Location: destination input"
    #Display "initial budget: budget input"
    #Display "Fuel: gas input"
    #Display "Accomodation: hotel input"
    #Display "Food: food input"
    #Display "total cost: sum of expenses"
    #Display "Remaining Balance: subtraction of all expenses from the budget"
