from os import system

# School management project
# Menu
from adminFunc import mainAdmin
from teacherFunc import mainTeacher
from studentFunc import mainStudent


print("\n*****************************************************************");
print("WELCOME TO OUR SCHOOL MANAGEMENT PROJECT");
print("*****************************************************************\n");

print("Please select your user role.\n")   
print("Press 1 if your are a admin")
print("Press 2 if your are a teacher")
print("Press 3 if your are a student\n")

role = input("what is your role? ")

if role == "1":
    system("clear")
    print("Welcome Admin!\n")
    mainAdmin()
elif role == "2":
    system("clear")
    print("Welcome Teacher!\n")
    mainTeacher()
elif role == "3":
    system("clear")
    print("Welcome Student!\n")
    mainStudent()
else:
    system("clear")
    print("Restart Application!")
    


    

