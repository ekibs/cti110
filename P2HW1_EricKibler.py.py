# This program calculates and displays travel expenses
    # 10/4/2022
    # CTI-110 P2HW1 - Travel
    # Eric Kibler
    #
# Pseudocode for Travel Expense
    #Get budget, location, gas, hotel, and food cost input from user
    #Program calculates the sum of expenses from user input
    #Program subtracts the expenses from the budget
    #Program displays all user inputs, how much the trip will cost, and how much money will be left over
print('This program calculates and displays travel expenses.\n')
userBudget = float(input('Enter Budget: \n'))
userDest = str(input('Enter your travel destination: \n'))
userGas = float(input('How much do you think you will spend on gas? \n'))
userHotel = float(input('Approximately, how much will you need for accomodation/hotel? \n'))
userFood = float(input('Last, how much do you need for food? \n'))
expenseSum = userGas + userHotel + userFood
print('------------Travel Expenses------------')
print('Location: ', end='')
print(userDest)
print('Initial Budget: $', end='')
print(userBudget)
print('Fuel: $', end='')
print(userGas)
print('Accomodation: $', end='')
print(userHotel)
print('Food: $', end='')
print(userFood)
print('Total cost: $', end='')
print(expenseSum)
print('----------------------------------------\n')
print('Remaining Balance: $', end='')
print(userBudget - expenseSum)
