##
#  Manage student grades.
#

# Use a dictionary named 'grades' to track student grades.
# code here
grades = {}

 
  # Loop until the user chooses to quit.
  # Check user input for the following "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? "
  # Prevent unexected inputs by converting input to upper-case
  # code here
user_input = ''
while (user_input != 'q' or 'Q'):
    user_input = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ").upper()
    
   # Use a condition to handle adding a new student.
   # Convert grade into integer
   # Gather user input for "Enter the name of the student: "
   # Check if student name already exists "Sorry, that student is already present."
   # Gather user input for student grade "Enter the student's grade: "
   # Validate input is in correct format or range, if not notify "Please enter grade as number 0-100"
   # code here
    match user_input:
        case 'A':
            student_name = input("Enter the name of the student: ")
            if student_name in grades:
                print("Sorry, that student is already present.")
            else:
                try:
                    student_grade = int(input("Enter the student's grade: "))
                    new_entry = {student_name : student_grade}
                    grades.update(new_entry)
                except ValueError:
                    print("Please enter grade as number from 1-100")
                

        case 'R':
            # Handle removing a student if user inputs 'R'
            # Check input for "What student do you want to remove? "
            # use pop to remove key/value form grades
            # see notes https://www.programiz.com/python-programming/methods/dictionary/pop
            # Check if student doesn't exist - "Sorry, that student doesn't exist and couldn't be removed."
            # code here
            remove_student = input("What student do you want to remove? ")
            if remove_student not in grades:
                print("Sorry, that student doesn't exist and couldn't be removed.")
            else:
                grades.pop(remove_student)
            
        case 'M':
               # Handle modifying a student grade if user inputs 'M'
               # "Enter the name of the student to modify: "
               # Convert grade into integer
               # If student is in grades dictionary, show existing grade "The old grade is"
               # Gather input for new grade "Enter the new grade: "
               # If student doesn't exist "Sorry, that student doesn't exist and couldn't be modified."
               # code here
               modify_student = input("Enter the name of the student to modify: ")
               if modify_student not in grades:
                   print("Sorry, that student doesn't exist and couldn't be modified")
               else:
                    print(f"The old grade is {grades.get(modify_student)}")
                    try:
                        student_grade = int(input("Enter the new grade: "))
                        new_entry = {modify_student : student_grade}
                        grades.update(new_entry)
                    except ValueError:
                        print("Please enter grade as number from 1-100")
                    
        case 'P':
                # Handle printing grade average as a string if user input is 'P'
                # Use "The average grade is "
                # Handle printing all of the student names with associated grade
                # Display explictly as strings
                # code here
                for key, value in grades.items():
                    print(f"{key}:{value}")
                values = grades.values()
                sum = sum(values)
                count = len(values)
                average = sum / count
                print(f"The average grade is {average}")

        case 'Q':
                # Handle the case for quiting if user inputs 'Q' "Goodbye!"
                # code here
                print("Goodbye!")
                break
        case _:
                # Handle the case of invalid input. "Sorry, that wasn't a valid choice."
                # code here
                print("Sorry, that wasn't a valid choice.")


   
 

   
 


 
   
 
      

  
 

   
 