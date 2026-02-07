from grade_compute import *

# function to calculate the student grade average
def grade_average(grades):
    return sum(grades)/len(grades)

# function to add a curve bonus to a student average
def curve_bonus(grades_list):
    average = round(grade_average(grades_list), 2)
    final = average + 0.25
    print(f"|  Curve Bonus:                    +0.25                       |")
    print(f"|  Final Letter Grade:             {numberToGrade(final)}                          |")
    print('---------------------------------------------------------------')


def main():
    # input loop
    while True:
        user_input = input("Please enter four letter grades (seperate each by '$') or press Q to quit. " ).upper()
        if user_input == 'Q':
            break
        grades = user_input.split('$')
        store_grades = []
        # store each grade inputted in a list
        for g in grades:
            print(gradeToNumber(g))
            num = gradeToNumber(g)
            store_grades.append(num)
        
        
        # output of all calculations done on store_grades
        print('---------------------------------------------------------------')
        print('|                   GRADE REPORT SUMMARY                       |')
        print('---------------------------------------------------------------')
        print(f'|  Grades Entered:                 {numberToGrade(store_grades[0])},{numberToGrade(store_grades[1])},{numberToGrade(store_grades[2])},{numberToGrade(store_grades[3])}                     |')
        print(f"|  Lowest Grade Dropped:           {numberToGrade(min(store_grades))}                           |")
        store_grades.sort()
        store_grades.pop(0)
        print(f"|  Calculated Average:             {round(grade_average(store_grades),2)}                         |")
        if all(g < 2.7 for g in store_grades):
            curve_bonus(store_grades)
        else:
            print(f"|  Final Letter Grade:             {numberToGrade(grade_average(store_grades))}                           |")
            print('---------------------------------------------------------------')

main() # call the main function 