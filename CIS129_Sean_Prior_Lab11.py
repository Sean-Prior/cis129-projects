# Sean Prior
# Nov 17th 2024
'''This program does something'''

sentinal = -1
# 9.1
def writeToPlainText():
    with open('grades.txt', 'w') as grades:
        while True:
            value = input('Give a grade of a student(-1 to quit):')
            try:
                value = int(value)
                if value == sentinal:
                    break
                elif value < sentinal:
                    print('Value too low, try again')
                else:
                    grades.write(f'{value}\n')
            except ValueError:
                print('That\'s not a valid value, try again')
            
writeToPlainText()

# 9.2
def readingFromPlainText():
    count = 0
    totalGrade = 0
    eaGrade = ''
    with open('grades.txt', 'r') as grades:
        for grade in grades:
            eaGrade += grade
            eaGrade = eaGrade.replace('\n', ' ')
            grade = int(grade)
            count += 1
            totalGrade += grade
    try:
        average = totalGrade / count
        print(f'There is a total of {count} grades')
        print(f'Each grade is {eaGrade}')
        print(f'All grades added up is {totalGrade}')
        print(f'The average for the student is {average:.2f}%')
    except ZeroDivisionError:
        print('No data was entered')
readingFromPlainText()

