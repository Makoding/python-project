import json
from elegxos import *
from teachers import *
from file_management import *

try:
    students = load_students_data()
except FileNotFoundError:
    save_students_data()
    students = load_students_data()

def menu():
    print("="*50)
    print("\t\tΜΕΝΟΥ ΕΠΙΛΟΓΩΝ")
    print("="*50)

    print("\n\n1.\tCreate a student registration")
    print("\n2.\tRead student(s) registrations")
    print("\n3\tUpdare student registration")
    print("\n4.\tDelete student registration")
    print("\n5.\tCreate a teacher registration")
    print("\n6.\tRead teacher(s) registrations")
    print("\n7.\tUpdare teacher registration")
    print("\n8.\tDelete teacher registration")
    
    print("\n9.\tExit the program.")


# 1st option in the main menu
def create_student():
    students = load_students_data()
    student = {}

    onoma = get_string("Give the name of the student that you want to registrate: ")
    epitheto = get_string("Give the surname of the student that you want to registrate: ")
    patronimo = get_string("Give the fathers name of the student that you want to registrate: ")
    student["name"] = onoma
    student["surname"] = epitheto
    student["fathersname"] = patronimo
    
    ilikia = get_integer("Give the age of the student that you want to registrate: ")
    student["age"] = ilikia

    taksi = get_integer("Give the class of the student that you want to registrate: ")
    student["class"] = taksi
    
    id_politi = get_integer("Give the id number of the student that you want to registrate: ")
    student["citizenid"] = id_politi
    print(students)
    id_mathiti = 1000 + len(students)
    student["studentid"] = id_mathiti
    
    save_students_data(student)
    students = load_students_data()
    print(f"\nStudent {epitheto} {onoma} of {patronimo} age {ilikia} years old who attends {taksi} class with citizen id number {id_politi} and student id number {id_mathiti} was succesfully registered to the system.")
    
    print(f"\n\t\t\tStudent Database:")
    for i in range(len(students)):
        for j in students[i].keys():
            print(f"{j}: {students[i][j]}")
        print("\n")

# 2nd option in the main menu        
def read_student():
    students = load_students_data()

    if len(students) == 0:
        print("There hasn't been a registeration on the students database yet. Please registerate a student first and come back later to read the list.")
        return False

    sub_menu()
    epilogi = get_integer_con(1, 3)

    
    if int(epilogi) == 1:
        entry = input("Type any of the personal info of the student that you want to print: ")
        print_output = []

        for i in range(len(students)):
            if students[i]["name"] == entry or students[i]["surname"] == entry or students[i]["fathersname"] == entry or students[i]["age"] == int(entry) or int(students[i]["class"]) == int(entry) or students[i]["citizenid"] == int(entry) or students[i]["studentid"] == int(entry):
                print_output.append(students[i])

        
        if len(print_output) == 1:
            print(f"The student based on the {entry} that you types has the personal info below:")
            print(print_output)
        elif len(print_output) > 1:
            print(f"The students based on the {entry} that you types has the personal info below:")
            for i in range(len(print_output)):    
                print(print_output[i])
        else:
            print("There is not such a student registrate in the system.  Returning to main menu...")
            return False
    
    elif int(epilogi) == 2:
        print_students_details()

    elif int(epilogi) == 3:
        print_students_names()

# 3rd option in the main menu
def update_student():
    students = load_students_data()
    print("1.Search the student based on surname.\n2.Search the student based on student id.")
    option = get_integer_con(1,2)

    if option == 1:
        while True:
            last_name = get_string("Give the surnamr of the student that you want to update: ")
            my_list = search_student_by_surname(last_name)
            if len(my_list) > 1:
                print("There is more than one student with this surname on the list.")
                for id in my_list:
                    for student in students:
                        if student["studentid"] == id:
                            print(student)
                
                id_option = get_integer("Choose one of the above students based on their student id: ")
                while id_option not in my_list:
                    id_option = get_integer("Choose one of the above students based on their student id: ")
                print(f"You chose {id_option}")                          

                for i in range(len(students)):
                    options_available = ["name", "surname", "fathersname", "age", "class", "citizenid"]
                    if students[i]["studentid"] == id_option:
                        update_option = get_string("Choose what you want to change in the specific registration (name, surname, fathersname, age, class, citizenid): ")
                        while update_option not in options_available:
                            update_option = get_string("Wrong Input. Choose what you want to change in the specific registration (name, surname, fathersname, age, class, citizenid): ")
                        change_student(update_option, i)

            elif len(my_list) == 1:
                for i in range(len(students)):
                    options_available = ["name", "surname", "fathersname", "age", "class", "citizenid"]
                    if students[i]["surname"] == last_name:
                        update_option = get_string("Choose what you want to change in the specific registration (name, surname, fathersname, age, class, citizenid): ")
                        while update_option not in options_available:
                            update_option = get_string("Wrong Input. Choose what you want to change in the specific registration (name, surname, fathersname, age, class, citizenid): ")
                        change_student(update_option, i)

                        
            elif len(my_list) == 0:
                print("There is not such a student registrate in the system.  Returning to main menu...")
                return False
            break
    if option == 2:
        id_option = search_student_by_id()
        for i in range(len(students)):
                    options_available = ["name", "surname", "fathersname", "age", "class", "citizenid"]
                    if students[i]["studentid"] == id_option:
                        update_option = get_string("Choose what you want to change in the specific registration (name, surname, fathersname, age, class, citizenid): ")
                        while update_option not in options_available:
                            update_option = get_string("Wrong Input. Choose what you want to change in the specific registration (name, surname, fathersname, age, class, citizenid): ")
                        change_student(update_option, i)



#4trh option of the main menu
def delete_student():
    students = load_students_data()
    print("1.Search the student based on surname.\n2.Search the student based on student id.")
    option = get_integer_con(1,2)

    if option == 1:
        while True:
            last_name = get_string("Give the surname of the student you want to delete: ")
            my_list = search_student_by_surname(last_name)
            if len(my_list) > 1:
                print("There is more than one student with this surname on the list.")
                for id in my_list:
                    for student in students:
                        if student["studentid"] == id:
                            print(student)
                
                id_option = get_integer("Choose one of the above students based on their student id: ")
                while id_option not in my_list:
                    id_option = get_integer("Choose one of the above students based on their student id: ")
                print(f"You chose {id_option}")
            
                delete_student_by_id(id_option)

            elif len(my_list) == 1:
                for i in range(len(students)):
                    if students[i]["surname"] == last_name:
                        students.pop(i)

            elif len(my_list) == 0:
                print("There is not such a stuednt registrate in the system.  Returning to main menu...")
                return False 
    elif option == 2:
        id_option = search_student_by_id()
        delete_student_by_id(id_option)

def sub_menu():

    print("="*60)
    print("PRINTING CHOICES MENU")
    print("="*60)

    print("\n1. Print student\n2. Print all the students (complete personal data)\n3. Print all the students (only names)")

def print_students_details():
    students = load_students_data()
    print(f"\n\t\t\tDatabase Μαθητών:")
    for i in range(len(students)):
        for j in students[i].keys():
            print(f"{j}: {students[i][j]}")
        print("\n")

def print_students_names():
    students = load_students_data()
    for i in range(len(students)):
        print(f"{students[i]["surname"]} {students[i]["name"]} with fathers name: {students[i]["fathersname"][0]}")
    

def next_id():
    students = load_students_data()
    if len(students) > 0:
        return f"Next available id is: {students[len(students)-1]["studentid"]+1}"
    else:
        return f"Next available id is: {1000}"
    
def search_student_by_surname(eponymo):
    students = load_students_data()
    id_list = []
    for i in range(len(students)):
        if students[i]["surname"] == eponymo:
            id_list.append(students[i]["studentid"])
    
    return id_list

def search_student_by_id():
    students = load_students_data()
    id_option = get_integer("Give the id of the student you want: ")
    while True:
        for student in students:
            if student["studentid"] == id_option:
                return id_option
        id_option = get_integer("There is no student with this id on the system, please insert again an id: ")

def delete_student_by_id(student_id):
    students = load_students_data()
    for i in range(len(students) - 1):
        if students[i]["studentid"] == student_id:
            students.pop(i)

def change_student(update_option,cnt):
    students = load_students_data()
                        
    if update_option == "name":
        change_option = get_string(f"You change the name from {students[cnt]["name"]} to: ")
        students[cnt]["name"] = change_option
    elif update_option == "surname":
        change_option = get_string(f"You change the surname from {students[cnt]["surname"]} to: ")
        students[cnt]["surname"] = change_option
    elif update_option == "fathersname":
        change_option = get_string(f"You change the fathers name from {students[cnt]["fathersname"]} to: ")
        students[cnt]["fathersname"] = change_option
    elif update_option == "age": 
        change_option = get_integer(f"You change the age from {students[cnt]["age"]} to: ")
        students[cnt]["age"] = change_option
    elif update_option == "class":
        change_option = get_integer(f"You change the class from {students[cnt]["class"]} to: ")
        students[cnt]["class"] = change_option
    elif update_option == "citizenid":
        change_option = get_integer(f"You change the citizen id number from {students[cnt]["citizenid"]} to: ")
        students[cnt]["citizenid"] = change_option

    alter_students_data(students)

def main():

    while True:
        menu()
        print(next_id())    
        
        choice = get_integer_con(1 ,9)

        if int(choice) == 1:
            create_student()
        elif int(choice) == 2:
            read_student()
        elif int(choice) == 3:
            update_student()
        elif int(choice) == 4:
            delete_student()
        elif int(choice) == 5:
            create_teacher()
        elif int(choice) == 6:
            read_teacher()
        elif int(choice) == 7:
            update_teacher()
        elif int(choice) == 8:
            delete_teacher()
        else:
            break



main()