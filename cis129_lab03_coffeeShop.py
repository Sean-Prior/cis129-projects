#This is the coffee shop
print("My Coffee and Muffin Shop")
coffeeQuestion = int(input("Number of coffees bought?\n"))
muffinQuestion = int(input("Number of muffins bought?\n"))
muffinCost = muffinQuestion * 4
coffeeCost = coffeeQuestion * 5
tax = (muffinCost + coffeeCost)*.06

print(coffeeQuestion, "Coffee at $5 each: ", coffeeCost)
print(muffinQuestion, "muffins at 4$ each: ", muffinCost)
print("6% tax: ", tax)
print("Total: $" , muffinCost + coffeeCost + tax)
