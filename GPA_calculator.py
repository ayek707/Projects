# This program calculates the user's unweighted GPA 
# based on the district grading scale

grade = '' 
string = ""
amount = 0
newGrade = 0
total_classes = 0
points = 0


#This while loop will run until the user enters "Done"
while True:
 
    # recieve grade from user
    grade = input("Grade: ")
    if grade == "Done":
        break
    
    try:
        amount = int(input("Amount of classes with this grade: "))
    except:
        print("Invalid input(s).")
        break


    # Handles number grades
    if grade.isnumeric():
        grade = int(grade)
        if grade >= 93:
            newGrade = 4
        elif grade >= 90:
            newGrade = 3.67
        elif grade >= 87:
            newGrade = 3.33
        elif grade >= 83:
            newGrade = 3 
        elif grade >= 80:
            newGrade = 2.67
        elif grade >= 77:
            newGrade = 2.33
        elif grade >= 73: 
            newGrade = 2
        elif grade >= 70:
            newGrade = 1.67
        elif grade >= 67:
            newGrade = 1.33
        elif grade >= 63:
            newGrade = 1
        elif grade >= 60:
            newGrade = 0.67
        elif grade < 60:
            newGrade = 0
        else: 
            print("Invalid input(s)")
            break
            
            
    # Handles letter grades 
    else:
       if grade == 'A':
            newGrade = 4
       elif grade == "A-":
            newGrade = 3.67
       elif grade == "B+":
            newGrade = 3.33
       elif grade == 'B': 
            newGrade = 3
       elif grade == 'B-':
            newGrade = 2.67
       elif grade == 'C+':
            newGrade = 2.33
       elif grade == 'C': 
            newGrade = 2
       elif grade == 'C-':
            newGrade = 1.67
       elif grade == 'D+': 
            newGrade = 1.33
       elif grade == 'D':
            newGrade = 1
       elif grade == 'D-': 
            newGrade = 0.67
       elif grade == 'F': 
            newGrade = 0
       else: 
            print("Invalid input(s)")
            break
            

    
    points += (newGrade * amount)
    total_classes += amount

  
# While loop ends 


#Calculates GPA 
if total_classes > 0:
   gpa = points / total_classes
    
   # If user has a gpa above a 3.97, it will be rounded
   # to 3 digits for better accuracy 
   if gpa < 3.97:
       gpa = round(gpa, 2)
       print("Your GPA: ", gpa)
   else:
       gpa = round(gpa, 3)
       print("Your GPA: ", gpa)
elif total_classes == 0: 
    print("Your GPA: 0")

        



    
    
