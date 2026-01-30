# function that converts letter grades to numeric values
def gradeToNumber(grade): 
    grade = grade.upper()
    if grade == 'A+':
        return 4.3
    elif grade == 'A':
        return 4
    elif grade == 'A-':
        return 3.7
    elif grade == 'B+':
        return 3.4
    elif grade == 'B':
        return 3
    elif grade == 'B-':
        return 2.7
    elif grade == 'C+':
        return 2.4
    elif grade == 'C':
        return 2
    elif grade == 'C-':
        return 1.7
    elif grade == 'D+':
        return 1.4
    elif grade == 'D':
        return 1
    elif grade == 'D-':
        return 0.7
    elif grade == 'F':
        return 0
    
# converts given numeric value to letter grade
def numberToGrade(grade):
    if grade == 4.3:
        return 'A+'
    elif grade == 4:
        return 'A'
    elif grade == 3.7:
        return 'A-'
    elif grade == 3.4:
        return 'B+'
    elif grade == 3:
        return 'B'
    elif grade == 2.7:
        return 'B-'
    elif grade == 2.4:
        return 'C+'
    elif grade == 2:
        return 'C'
    elif grade == 1.7:
        return 'C-'
    elif grade == 1.4:
        return 'D+'
    elif grade == 1:
        return 'D'
    elif grade == 0.7:
        return 'D-'
    elif grade == 0:
        return 'F'
    
    

