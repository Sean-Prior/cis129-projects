# CIS129 Module 4 Lab-4
# Sean Prior
# Sept 29 2024
'''This program calculates a stores monthly sales and calculates how much\
    the stores bonus will be based on it's monthly sales. Additionally, \
    they use a % of sales increase to give employees a small bonus to their pay.'''
# The main function
def main():
# Declares the local variables
    monthlySales = getSales()
    salesIncrease = getIncrease()
    storeAmount = calcStoreBonus(monthlySales)
    empAmount = calcEmpBonus(salesIncrease)
    printBonus(storeAmount,empAmount)
# This function gets the monthly sales
def getSales():
 monthlySales = float(input('What\'s the monthly sales: '))
 return monthlySales
 
# This function gets the percent of increase in sales
def getIncrease():
    salesIncrease = float(input('What\'s the sales increase: '))
    salesIncrease = salesIncrease / 100
    return salesIncrease
def calcStoreBonus(monthlySales):
    if (monthlySales >= 110000):
        storeAmount = 6000
    elif (monthlySales >= 100000):
        storeAmount = 5000
    elif (monthlySales >= 90000):
        storeAmount = 4000
    elif (monthlySales >= 80000):
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount
# This function determines the empAmount bonus
def calcEmpBonus(salesIncrease):
    if (salesIncrease >= .05):
        empAmount = 75
    elif (salesIncrease >= .04):
        empAmount = 50
    elif (salesIncrease >= .03):
        empAmount = 40
    else:
        empAmount = 0
    return empAmount
# This function prints the bonus information
def printBonus(storeAmount,empAmount):
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    if (storeAmount == 6000 )and(empAmount == 75):
        print('Congrats! You have reached the highest bonus amounts \
possible! ')
 
# calls main
main()
