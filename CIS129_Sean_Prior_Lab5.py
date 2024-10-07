# Sean Prior
# Oct 7, 2024
# This program will ask how many bottles were collected over a week and how much is made off each bottle

def main():
    keep_going = 'y'
    while keep_going == 'y':
        total_bottles = get_bottles()
        total_payout = get_payout(total_bottles)
        print_info(total_bottles, total_payout)
        print('Do you want to enter another week\'s worth of data?')
        keep_going = input('Enter y or n: ')
def get_bottles():
    counter = 1
    total_bottles = 0
    today_bottles = 0
    while counter <= 7:
        today_bottles = int(input('How many bottles were there on day ' + str(counter) +\
                                  '? '))
        counter += 1
        total_bottles += today_bottles
    return total_bottles
def get_payout(total_bottles):
    total_payout = 0
    total_payout = total_bottles * .1
    return total_payout
def print_info(total_bottles, total_payout):
    print('The total number of bottles collected is', total_bottles)
    print(f'The total paid out is $ {total_payout:.2f}')
main()
