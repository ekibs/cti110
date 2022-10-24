# CTI-110
# P3HW2 - Salary
# Eric Kibler
# 10-24-2022
#

#Pseudocode
    #Get employee name input
    #Get employee hours worked and pay rate input
    #Program calculates if the employee has worked overtime and calculates extra overtime pay if the employee has worked over 40 hours
    #Program calculates how much money the employee has earned 
    #Program displays employee name, pay rate, hours worked, overtime hours worked, regular pay, overtime pay, and gross pay

employee = str(input("Enter employee's name: "))
hours = float(input('Enter number of hours worked: '))
payRate = float(input("Enter employee's pay rate: "))
overtimeHours = hours - 40
regHours = hours - overtimeHours
regPay = regHours * payRate

if hours > 40:
    overtimePay = (payRate * 1.5) * overtimeHours
else:
    overtimePay = 0

gross = regPay + overtimePay

print('------------------------------------')
print('Employee name: ',    employee)
print()
print('Hours Worked', end='   ') 
print('Pay Rate', end='   ') 
print('OverTime', end='   ')
print('OverTime Pay', end='       ')
print('RegHour Pay', end='        ')
print('Gross Pay')
print('---------------------------------------------------------------------------------------------------')
print(hours, end='           ')
print(payRate, end='       ')
print(overtimeHours, end='        ')
print(f'${overtimePay:.2f}', end='            ')
print(f'${regPay:.2f}', end='            ')
print(f'${gross:.2f}')