# Sean Prior
# Nov 17th 2024
'''This program gets grades from the user and stores them in a txt file for later use
Then those grades are called from the txt file later in the program to get an average
Lastly, we ask for a students first and last name aswell as their 3 exam grades to store in a csv file'''

sentinal = -1 # universal exit
# 9.1
def writeToPlainText(): # gets plain grades from the user
    with open('grades.txt', 'w') as grades: # opens grades.txt for writing
        while True: # keeps looping
            value = input('Give a grade of a student(-1 to quit):')
            try:
                value = int(value)
                if value == sentinal: # exits the loop when user is finished
                    break
                elif value < sentinal: # checks if the input is below the sentinal
                    print('Value too low, try again')
                else:
                    grades.write(f'{value}\n') # writes the input grade in grades.txt file
            except ValueError: # checks if it's a number
                print('That\'s not a valid value, try again')
            
writeToPlainText()

# 9.2
def readingFromPlainText(): # pulls grades stored in grades.txt
    count = 0
    totalGrade = 0
    eaGrade = ''
    with open('grades.txt', 'r') as grades: # opens grades.txt for reading
        for grade in grades: # pulls each grade from grades.txt
            eaGrade += grade # holds each grade as a string
            eaGrade = eaGrade.replace('\n', '% ') # cleans up the string
            grade = int(grade) # converts to an int for math later
            count += 1 # needed to get the average
            totalGrade += grade # gets all grades added together
    try:
        average = totalGrade / count # gets average
        # prints the results
        print(f'There is a total of {count} grades')
        print(f'Each grade is {eaGrade}')
        print(f'All grades added up is {totalGrade}')
        print(f'The average for the student is {average:.2f}%')
    except ZeroDivisionError: # checks if no data was entered
        print('No data was entered\n')
readingFromPlainText()

# 9.3
import csv # needed for csv to work

def writingToCSVFile():
    studentCount = 0
    with open('grades.csv', 'w', newline='') as grades: # opens grades.csv for writing
        writer = csv.writer(grades) # needed to write to the csv file
        while True:
            print(f'Total students added is {studentCount} so far')
            firstName = input('Enter the students first name(-1 to quit adding students):') # get first name
            try:
                firstName = int(firstName) # converts a number into an int for potential exit
                if firstName == sentinal: # exit the loop
                    break
                else:
                    firstName = str(firstName) # convert back into string if input isn't -1
            except ValueError: # needed to prevent an error with trying to convert letters into an int
                None
            lastName = input('Enter the students last name:') # get last name
            if(not firstName.isalpha() or not lastName.isalpha()): # checks if the input name makes sense
                print('What kind of name is that? Letters only \n')
                continue # restarts the loop
            try:
                # gets all 3 exam scores from the user as int
                exam1 = int(input('Enter the students first exam score:'))
                exam2 = int(input('Enter the students second exam score:'))
                exam3 = int(input('Enter the students third exam score:'))
                studentCount += 1
            except ValueError: # checks if the exam score input is a number
                print('Invalid value, student wasn\'t added, try again please. Try again \n')
                continue # restarts the loop
            writer.writerow([firstName, lastName, exam1, exam2, exam3]) # writes your polished input to the csv file
writingToCSVFile()
