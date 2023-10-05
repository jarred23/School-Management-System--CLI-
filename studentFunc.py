from os import system

def mainStudent():
    print("Press 1 to read homework!")
    print("Press 2 to read assessment dates!")
    print("Press 3 to read exam timetable!")
    print("Press 4 to read sport days!")
    print("Press 5 to read study guides!\n")

    secondMenu = input("Enter your choice: ")

    if secondMenu == "1":
        system("clear")
        readHomework()  
    elif secondMenu == "2":
        system("clear")
        readAssessments()
    elif secondMenu == "3":
        system("clear")
        readExamTimeTable()
    elif secondMenu == "4":
        system("clear")
        readSportDays()
    elif secondMenu == "5":
        system("clear")
        readStudyGuides()
    else:
        system("clear")
        print("Please enter a valid number!")

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."

def readHomework():
    grade_choice = input("Enter grade (8 - 12): ")
    filename = f"txt_File/HomeWork/homework_grade_{grade_choice}.txt"
    content = read_file(filename)
    print(content)
    input("Press any key to continue 'BACK': ")
    system("clear")
    mainStudent()

def readAssessments():
    grade_choice = input("Enter grade (8 - 12): ")
    filename = f"txt_File/Assessments/Assessments_grade_{grade_choice}.txt"
    content = read_file(filename)
    print(content)
    input("Press any key to continue 'BACK': ")
    system("clear")
    mainStudent()


def readExamTimeTable():
    grade_choice = input("Enter grade (8 - 12): ")
    filename = f"txt_File/Exam_Time_Table/ExamTimeTable_grade_{grade_choice}.txt"
    content = read_file(filename)
    print(content)
    input("Press any key to continue 'BACK': ")
    system("clear")
    mainStudent()


def readSportDays():
    grade_choice = input("Enter grade (8 - 12): ")
    filename = f"txt_File/SportDays/sport_days_grade_{grade_choice}.txt"
    content = read_file(filename)
    print(content)
    input("Press any key to continue 'BACK': ")
    system("clear")
    mainStudent()


def readStudyGuides():
    grade_choice = input("Enter grade (8 - 12): ")
    filename = f"txt_File/StudyGui/studyGuides_grade_{grade_choice}.txt"
    content = read_file(filename)
    print(content)
    input("Press any key to continue 'BACK': ")
    system("clear")
    mainStudent()


