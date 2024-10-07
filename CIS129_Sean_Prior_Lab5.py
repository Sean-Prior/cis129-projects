# Sean Prior
# Oct 7, 2024
''' This program will ask how many bottles were collected over a week and how much is made off all bottles\
then asks if there's another week the user would like to input into the system to be calculated'''

def main():
    keep_going = 'y'
    while keep_going == 'y': # used to ask if the user would like to input another week of bottle collection
        total_bottles = get_bottles()
        total_payout = get_payout(total_bottles)
        print_info(total_bottles, total_payout)
        print('Do you want to enter another week\'s worth of data?')
        keep_going = input('Enter y or n: ')
def get_bottles(): # asks the user for required bottle amount to run the script
    # the 3 variables needed to get the bottles
    counter = 1
    total_bottles = 0
    today_bottles = 0
    while counter <= 7: # asks for amount of bottles each day of a week and adds them up
        today_bottles = int(input('Enter number of bottles for day #' + str(counter) +\
                                  ': '))
        counter += 1 # adds 1 to the current counter, needed to exit the while loop after 7
        total_bottles += today_bottles # adds each bottle entry together
    return total_bottles # returns total bottle amount needed for calculation
def get_payout(total_bottles): # gets the payout from amount of bottles
    total_payout = 0
    total_payout = total_bottles * .1
    return total_payout # returns payout from amount of bottles
def print_info(total_bottles, total_payout): # pulls the total bottles & payout to print
    print('The total number of bottles collected is', total_bottles) # prints the total bottles
    print(f'The total paid out is $ {total_payout:.2f}') # prints the total payout
main() # calls the main to start
