# Sean Prior
# This is the coffee shop lab
# Asks the user how many muffins and coffees they want, then gives them the total.
print("***************************************")
print("My Coffee and Muffin Shop")
# This creates the integers and required inputs from the user for the coffee shop
coffeeQuestion = int(input("Number of coffees bought?\n"))
muffinQuestion = int(input("Number of muffins bought?\n"))
teaQuestion = int(input("Number of teas bought?\n"))
bagelQuestion = int(input("Number of bagels bought?\n"))
print("***************************************\n")
# This does the required math to get the correct value for the coffee shop
muffinCost = muffinQuestion * 4
coffeeCost = coffeeQuestion * 5
teaCost = teaQuestion * 3
bagelCost = bagelQuestion * 5
# Calculates the 6% tax added on
tax = (muffinCost + coffeeCost + teaCost + bagelCost)*.06
# This prints the totals like a receipt at an actual coffee shop
print("***************************************")
print(coffeeQuestion, "Coffee at $5 each: $", coffeeCost)
print(muffinQuestion, "muffins at 4$ each: $", muffinCost)
print(teaQuestion, "tea at $3 each: $", teaCost)
print(bagelQuestion, "bagel at $5 each: $", bagelCost)
print("6% tax: ", tax)
print("---------")
# Total cost of all items
print("Total: $" , muffinCost + coffeeCost + teaCost + bagelCost + tax)
print("***************************************")
