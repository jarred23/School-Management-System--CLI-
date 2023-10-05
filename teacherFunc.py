from os import system

def mainTeacher():
    print("Press 1 to enter homework for students:")
    print("Press 2 to enter assessment dates for students:")
    print("Press 3 to enter exam timetable for students:")
    print("Press 4 to enter sport days for students:")
    print("Press 5 to enter study guides for students:\n")

    secondMenu = input("Enter your choice: ")

    if secondMenu == "1":
        system("clear")
        HomeWork()  
    elif secondMenu == "2":
       system("clear")
       assessments()
    elif secondMenu == "3":
        system("clear")
        Exam_Time_Table()
    elif secondMenu == "4":
        system("clear")
        SportDays()
    elif secondMenu == "5":
        system("clear")
        studyGuides()
    else:
        system("clear")
        print("Please enter a valid number!")







# External functions to call

    # HOMEWORK PART IF U CALL OPTION 1
def HomeWork():
    grade_options = ["8", "9", "10", "11", "12"]
    print("Select a grade (8 - 12): (The grade NOT the number!)\n")
    for i, grade in enumerate(grade_options, start=1):
        print(f"{i}. Grade {grade}")

    grade_choice = input("\nEntered grade number: ")

    if grade_choice in grade_options:
        homework_text = input(f"Enter homework for Grade {grade_choice} students: ")
        print(f"\nHomework for Grade {grade_choice}: {homework_text}")

        filename = f"txt_File/HomeWork/homework_grade_{grade_choice}.txt"
        with open(filename, "a") as file:
            file.write(homework_text + "\n")
            print(f"Homework for Grade {grade_choice} saved to {filename}")
            mainTeacher()
    else:
        print("Invalid grade choice!")

    # ASSESSMENTS PART IF U CALL OPTION 2
def assessments():
    grade_options = ["8", "9", "10", "11", "12"]
    print("Select a grade (8 - 12): (The grade NOT the number!)\n")
    for i, grade in enumerate(grade_options, start=1):
        print(f"{i}. Grade {grade}")

    grade_choice = input("\nEntered grade number: ")

    if grade_choice in grade_options:
        assessments_text = input(f"Enter assessments dates for Grade {grade_choice} students: ")
        print(f"\nAssessment dates for Grade {grade_choice}: {assessments_text}")

        filename = f"txt_File/Assesments/Assessments_grade_{grade_choice}.txt"
        with open(filename, "a") as file:
            file.write(assessments_text + "\n")
            print(f"Assessments for Grade {grade_choice} saved to {filename}")
            mainTeacher()
    else:
        print("Invalid grade choice!")
        
    # EXAM TIME TABLE IF U CALL OPTION 3
def Exam_Time_Table():
    grade_options = ["8", "9", "10", "11", "12"]
    print("Select a grade (8 - 12): (The grade NOT the number!)\n")
    for i, grade in enumerate(grade_options, start=1):
        print(f"{i}. Grade {grade}")

    grade_choice = input("\nEntered grade number: ")

    if grade_choice in grade_options:
        ExamTimeTable_text = input(f"Enter Exam TimeTable for Grade {grade_choice} students: ")
        print(f"\nExam timetable for Grade {grade_choice}: {ExamTimeTable_text}")

        filename = f"txt_File/Exam_Time_Table/ExamTimeTable_grade_{grade_choice}.txt"
        with open(filename, "a") as file:
            file.write(ExamTimeTable_text + "\n")
            print(f"Exam time table for Grade {grade_choice} saved to {filename}")
            mainTeacher()
    else:
        print("Invalid grade choice!")
       
    # SPORT DAYS PART IF U CALL OPTION 4
def SportDays():
    grade_options = ["8", "9", "10", "11", "12"]
    print("Select a grade (8 - 12): (The grade NOT the number!)\n")
    for i, grade in enumerate(grade_options, start=1):
        print(f"{i}. Grade {grade}")

    grade_choice = input("\nEntered grade number: ")

    if grade_choice in grade_options:
        Sport_days_text = input(f"Enter Sport-day for Grade {grade_choice} students: ")
        print(f"\nHomework for Grade {grade_choice}: {Sport_days_text}")

        filename = f"txt_File/SportDays/sport_days_grade_{grade_choice}.txt"
        with open(filename, "a") as file:
            file.write(Sport_days_text + "\n")
            print(f"Sport days for Grade {grade_choice} saved to {filename}")
            mainTeacher()
    else:
        print("Invalid grade choice!")
        
    #STUDY GUIDES PART IF U CALL OPTION 5
def studyGuides():
    grade_options = ["8", "9", "10", "11", "12"]
    print("Select a grade (8 - 12): (The grade NOT the number!)")
    for i, grade in enumerate(grade_options, start=1):
        print(f"{i}. Grade {grade}")

    grade_choice = input("\nEnter the grade number: ")

    if grade_choice in grade_options:
        Study_guides_text = input(f"\nEnter Study guides for Grade {grade_choice} students: ")
        print(f"\nStudy guides for Grade {grade_choice}: {Study_guides_text}")

        filename = f"txt_File/StudyGui/studyGuides_grade_{grade_choice}.txt"
        with open(filename, "a") as file:
            file.write(Study_guides_text + "\n")
            print(f"Study guides for Grade {grade_choice} saved to {filename}")
            mainTeacher()
    else:
        print("Invalid grade choice!")