from grade_compute import *

def grade_average(grades):
    return sum(grades)/len(grades)

while True:
    user_input = input("Please enter four letter grades (seperate each by '$') or press Q to quit. " ).upper()
    if user_input == 'Q':
        break
    grades = user_input.split('$')
    store_grades = []
    for g in grades:
        print(gradeToNumber(g))
        num = gradeToNumber(g)
        store_grades.append(num)
    
    

    print('-' * 50)
    print('|        GRADE REPORT SUMMARY        |')
    print('-' * 50)
    print(f'|  Grades Entered: {numberToGrade(store_grades[0])},{numberToGrade(store_grades[1])},{numberToGrade(store_grades[2])},{numberToGrade(store_grades[3])}      |')
    print(f"|  Lowest Grade Dropped: {min(store_grades)}")
    store_grades.sort()
    store_grades.pop(0)
    print(f"|  Calculated Average:  {grade_average(store_grades)}")
    if all(g < 2.7 for g in store_grades):
        average = grade_average(store_grades)
        final = average + 0.25
        print(f"|  Curve Bonus:   +0.25  |")
        print(f"|  Final Letter Grade: {numberToGrade(final)}")
    else:
        print(f"|  Final Letter Grade: {numberToGrade(grade_average(store_grades))}")
