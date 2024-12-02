# Sean Prior
# Nov 26th 2024
'''This program creates a class pet with three atributes, it's name, type, and age'''
class pet: # creates the class pet
    def __init__(self, name, breed, age): # Creates 3 atributes for the constructor
        self.name = name
        self.breed = breed
        self.age = age
    def setName(self):
        while True: # Keeps looping until break
            self.name = input('Enter your pet\'s name:\n') # Gets user input about pet name
            name = self.name
            if(not name.isalpha()): # Checks if the input has anything other than letters
                print('That\'s a weird name, give a better one.')
            else:
                break
        return name
    def setType(self): # Sets the type of animal your pet is
        while True: # keeps looping until break
            self.breed = input('Enter your pet\'s type:\n') # Gets user input about type of pet
            breed = self.breed
            if(not breed.isalpha()): # Checks if the input has anything other than letters
                print('That doesn\'t sound like a type of animal, try again.')
            else:
                break
        return breed
    def setAge(self): # Sets the age of the pet
        while True: # Keeps looping until break
            try: # Input validation
                self.age = int(input('Enter your pet\'s age:\n')) # Gets user input about pet age
                break
            except ValueError:
                print('invalid age, please input a valid age')
                continue
        return self.age
    def getName(self): # Returns the name of the pet
        return self.name
    def getType(self): # Returns the type of pet
        return self.breed
    def getAge(self): # Returns the pets age
        return self.age
yourPet = pet('name', 'breed', 0) # Constructor, passes to __init__, values will be changed later
yourPet.setName() # Calls to set the name of your pet
yourPet.setType() # Calls to set the type of animal of your pet
yourPet.setAge() # Calls to set the age of your pet
print('Your pet\'s name is', yourPet.getName()) # Gets the name of your pet and prints it
print('Your pet\'s type is', yourPet.getType()) # Gets the type of your pet and prints it
print('Your pet\'s age is', yourPet.getAge()) # Gets the age of your pet and prints it
