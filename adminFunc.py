from os import system

def mainAdmin():
    while True:
        print("\nPress 1 to add a teacher")
        print("Press 2 to add a student")
        print("Press 3 to read teachers")
        print("Press 4 to read students")
        print("Press 5 to exit")
        
        choice = input()
        
        if choice == "1":
            add_teacher()
        elif choice == "2":
            add_student()
        elif choice == "3":
            read_teachers()
        elif choice == "4":
            read_students()
        elif choice == "5":
            print("Exiting admin menu.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    mainAdmin()





#  EXTERNAL FUNCTION TO CALL

teachers = []
students = []

# Function to add a teacher

def add_teacher():
    system("clear")
    teacher_name = input("Please enter teacher name: ")
    grade_of_teaching = input("Please enter the grade of teaching: ")
    teachers.append({"Name": teacher_name, "Grade of Teaching": grade_of_teaching})
    save_teachers_to_file() 
    print("Teacher added successfully!")
    input("Please enter anything to continue!")
    system("clear")
    mainAdmin()

# Function to add a student
def add_student():
    system("clear")
    student_name = input("Please enter student name: ")
    student_grade = input("Please enter student grade: ")
    students.append({"Name": student_name, "Grade": student_grade})
    save_students_to_file()  
    print("Student added successfully!")
    input("Please enter anything to continue!")
    system("clear")
    mainAdmin()

# Function to save teachers to a text file
def save_teachers_to_file():
    with open("txt_File/admin/teachers.txt", "w") as file:
        for teacher in teachers:
            file.write(f"Name: {teacher['Name']}, Grade of Teaching: {teacher['Grade of Teaching']}\n")

# Function to save students to a text file
def save_students_to_file():
    with open("txt_File/admin/students.txt", "w") as file:
        for student in students:
            file.write(f"Name: {student['Name']}, Grade: {student['Grade']}\n")

# Function to read all teachers from the text file
def read_teachers():
    print("\nList of Teachers:")
    with open("txt_File/admin/teachers.txt", "r") as file:
        for line in file:
            print(line.strip())

# Function to read all students from the text file
def read_students():
    print("\nList of Students:")
    with open("txt_File/admin/students.txt", "r") as file:
        for line in file:
            print(line.strip())

