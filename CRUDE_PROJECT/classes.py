import json
from elegxos import *

students_file = "students_data.json"
teachers_file = "teachers_data.json"

def sub_student_menu():

    print("="*60)
    print("PRINTING CHOICES MENU FOR STUDENTS")
    print("="*60)

    print("\n1. Printing student\n2. Print all the students (analytic)\n3. Print all the students (only names)")

def sub_teacher_menu():

    print("="*60)
    print("PRINTING CHOICES MENU FOR TEACHERS")
    print("="*60)

    print("\n1. Printing teacher\n2. Print all the teachers (analytic)\n3. Print all the teachers (only names)")

class Students:
    def __init__(self):
        empty_list = []
        try:
            with open(students_file, "r") as f:
                self.students_list = json.load(f)
        except FileNotFoundError:
            with open(students_file, "w") as f:
                self.students_list = json.dump(empty_list,f)
            with open(students_file, "r") as f:
                self.students_list = json.load(f)

    def save_students_data(self):
        with open(students_file, "w") as f:
            self.students_list = json.dump(self.students_list,f)
        with open(students_file, "r") as f:
                self.students_list = json.load(f)

    def next_id(self):
        print(f"Next id for students: {1000+len(self.students_list)}")

#1st option in the main menu
    def create_student(self):
        student = {}
        name = get_string("Give the name of the student that you want to registrate: ")
        surname = get_string("Give the surname of the student that you want to registrate: ")
        fathers_name = get_string("Give the fathers name of the student that you want to registrate: ")
        
        student["name"] = name
        student["surname"] = surname
        student["fathersname"] = fathers_name
        
        age = get_integer("Give the age of the student that you want to registrate: ")
        student["age"] = age

        classroom = get_integer("Give the class of the student that you want to registrate: ")
        student["class"] = classroom
        
        citizenid = get_integer("Give the id number of the student that you want to registrate: ")
        student["citizenid"] = citizenid

        if len(self.students_list) == 0:
            studentid = 1000
        else:
            studentid = 1001
            i = 0
            while i < len(self.students_list):
                print(i)
                if self.students_list[i]["studentid"] == studentid:
                    i=0 
                    studentid += 1
                i += 1        

        student["studentid"] = studentid
        self.students_list.append(student)

        self.save_students_data()

        
    
#2nd option in the main menu
    def read_student(self):
        if len(self.students_list) == 0:
            print("There hasn't been a registeration on the students database yet. Please registerate a student first and come back later to read the list.")
            return False
    
        sub_student_menu()
        choice = get_integer_con(1, 3)
        
        
        if int(choice) == 1:
            entry = input("Please type any of the elements of the student that you want to print: ")
            print_output = []

            for i in range(len(self.students_list)):
                    if entry.isalpha():
                        if self.students_list[i]["name"] == entry or self.students_list[i]["surname"] == entry or self.students_list[i]["fathersname"] == entry :
                            print_output.append(self.students_list[i])
                    elif entry.isdigit():
                        if self.students_list[i]["class"] == int(entry) or self.students_list[i]["age"] == int(entry) or self.students_list[i]["citizenid"] == int(entry) or self.students_list[i]["studentid"] == int(entry):
                            print_output.append(self.students_list[i])
        
            
            
            if len(print_output) == 1:
                print(f"Student based on the {entry} you typed has this personal info:")
                print(print_output)
            elif len(print_output) > 1:
                print(f"Student based on the {entry} you typed has these personal infos:")
                for i in range(len(print_output)):    
                    print(print_output[i])
            else:
                print("Couldnt found a student based on the element you typed.")
        
        elif int(choice) == 2:
            self.print_students_details()

        elif int(choice) == 3:
            self.print_students_names()

#3rd option in the main menu
    def update_student(self):
            
        print("1.Search students based on surname.\n2.Search students based on id.")
        option = get_integer_con(1,2)

        if option == 1:
            while True:
                last_name = get_string("Give the surname of the student that you want to update: ")
                my_list = self.search_student_by_surname(last_name)
                if len(my_list) > 1:
                    print("There are more than one student with this surname on the list.")
                    for id in my_list:
                        for student in self.students_list:
                            if student["studentid"] == id:
                                print(student)
                    
                    id_option = get_integer("Choose one of the above students based on threir studentid: ")
                    while id_option not in my_list:
                        id_option = get_integer("Choose one of the above student based on threir studentid: ")
                    print(f"You chose: {id_option}")

                    for i in range(len(self.students_list)):
                        options_available = ["name", "surname", "fathersname", "age", "class", "citizenid"]
                        if self.students_list[i]["studentid"] == id_option:
                            update_option = get_string("Choose what you want to change in this registration(name, surname, fathersname, age, class, citizenid): ")
                            while update_option not in options_available:
                                update_option = get_string("Wrong, input. Choose what you want to change in this registration (name, surname, fathersname, age, class, citizenid): ")
                            self.change_student(update_option, i)
                            
                elif len(my_list) == 1:
                    for i in range(len(self.students_list)):
                        options_available = ["name", "surname", "fathersname", "age", "class", "citizenid"]
                        if self.students_list[i]["surname"] == last_name:
                            update_option = get_string("Choose what you want to change in this registration (name, surname, fathersname, age, class, citizenid): ")
                            while update_option not in options_available:
                                update_option = get_string("Wrong input. Choose what you want to change in this registration (name, surname, fathersname, age, class, citizenid): ")
                            self.change_student(update_option, i)

                elif len(my_list) == 0:
                    print("There isn't such a student registered in the system. Return back to main menu...")
                    return False
                break
        if option == 2:
            id_option = self.search_student_by_id()
            for i in range(len(self.students_list)):
                        options_available = ["name", "surname", "fathersname", "age", "class", "citizenid"]
                        if self.students_list[i]["studentid"] == id_option:
                            update_option = get_string("Choose what you want to change in this registration (name, surname, fathersname, age, class, citizenid): ")
                            while update_option not in options_available:
                                update_option = get_string("Wrong input. Choose what you want to change in this registration (name, surname, fathersname, age, class, citizenid): ")
                            self.change_student(update_option, i)

#4th option in the main menu
    def delete_student(self):

        print("1.Search students based on surname.\n2.Search students based on id.")
        option = get_integer_con(1,2)

        if option == 1:
            while True:
                last_name = get_string("Give the surname of the student that you want to delete: ")
                my_list = self.search_student_by_surname(last_name)
                if len(my_list) > 1:
                    print("There are more than one student with this surname on the list.")
                    for id in my_list:
                        for student in self.students_list:
                            if student["studentid"] == id:
                                print(student)
                    
                    id_option = get_integer("Choose one of the above students based on their studentid: ")
                    while id_option not in my_list:
                        id_option = get_integer("Choose one of the above students based on their studentid: ")
                    print(f"You chose: {id_option}")
                
                    self.delete_student_by_id(id_option)

                elif len(my_list) == 1:
                    for i in range(len(self.students_list)):
                        if self.students_list[i]["surname"] == last_name:
                            self.students_list.pop(i)

                elif len(my_list) == 0:
                    print("There isn't such a student registered in the system. Return back to main menu...")
                    return False 
        elif option == 2:
            id_option = self.search_student_by_id()
            self.delete_student_by_id(id_option)

    def print_students_details(self):
        print(f"\n\t\t\tStudents Database:")
        for i in range(len(self.students_list)):
            for j in self.students_list[i].keys():
                print(f"{j}: {self.students_list[i][j]}")
            print("\n")

    def print_students_names(self):
        
        for i in range(len(self.students_list)):
            print(f"{self.students_list[i]["surname"]} {self.students_list[i]["name"]} του {self.students_list[i]["fathersname"][0]}")

    def delete_student_by_id(self, student_id):
        for i in range(len(self.students_list) - 1):
            if self.students_list[i]["studentid"] == student_id:
                self.students_list.pop(i)
        self.save_students_data()
    
    def search_student_by_id(self):
        id_option = get_integer("Give the student id of the student you want: ")
        while True:
            for student in self.students_list:
                if student["studentid"] == id_option:
                    return id_option
            id_option = get_integer("There is not a student with this id on the system, please insert again a student id number")

    def search_student_by_surname(self, last_name):
        id_list = []
        for i in range(len(self.students_list)):
            if self.students_list[i]["surname"] == last_name:
                id_list.append(self.students_list[i]["studentid"])
        return id_list

    def change_student(self, update_option, cnt):

        if update_option == "name":
            change_option = get_string(f"You change the name from {self.students_list[cnt]["name"]} to: ")
            self.students_list[cnt]["name"] = change_option
        elif update_option == "surname":
            change_option = get_string(f"You change the surname from {self.students_list[cnt]["surname"]} to: ")
            self.students_list[cnt]["surname"] = change_option
        elif update_option == "fathersname":
            change_option = get_string(f"You change the surname from {self.students_list[cnt]["fathersname"]} to: ")
            self.students_list[cnt]["fathersname"] = change_option
        elif update_option == "age": 
            change_option = get_integer(f"You change the age from {self.students_list[cnt]["age"]} to: ")
            self.students_list[cnt]["age"] = change_option
        elif update_option == "class":
            change_option = get_string(f"You change the subject from {self.students_list[cnt]["subject"]} to: ")
            self.students_list[cnt]["class"] = change_option
        elif update_option == "citizenid":
            change_option = get_integer(f"You change the citizen id from {self.students_list[cnt]["citizenid"]} to:")
            self.students_list[cnt]["citizenid"] = change_option
        
        self.save_students_data()


class Teachers:
    def __init__(self):
        empty_list = []
        try:
            with open(teachers_file, "r") as f:
                self.teachers_list = json.load(f)
        except FileNotFoundError:
            with open(teachers_file, "w") as f:
                self.teachers_list = json.dump(empty_list,f)
            with open(teachers_file, "r") as f:
                self.teachers_list = json.load(f)

    def save_teachers_data(self):
        with open(teachers_file, "w") as f:
            self.teachers_list = json.dump(self.teachers_list,f)
        with open(teachers_file, "r") as f:
                self.teachers_list = json.load(f)

    def next_id(self):
        print(f"Next id for teachers: {1000+len(self.teachers_list)}")

#5th option in the main menu
    def create_teacher(self):
        teacher = {}
        name = get_string("Give the name of the teacher that you want to registrate: ")
        surname = get_string("Give the surname of the teacher that you want to registrate: ")
        fathers_name = get_string("Give the fathers name of the teacher that you want to registrate: ")
        
        teacher["name"] = name
        teacher["surname"] = surname
        teacher["fathersname"] = fathers_name
        
        age = get_integer("Give the age of the teacher that you want to registrate: ")
        teacher["age"] = age

        subject = get_string("Give the subject of the teacher that you want to registrate: ")
        teacher["subject"] = subject
        
        citizenid = get_integer("Give the id number of the teacher that you want to registrate: ")
        teacher["citizenid"] = citizenid

        if len(self.teachers_list) == 0:
            teacherid = 1000
        else:
            teacherid = 1001
            i = 0
            while i < len(self.teachers_list):
                print(i)
                if self.teachers_list[i]["teacherid"] == teacherid:
                    i=0 
                    teacherid += 1
                i += 1        
        teacher["teacherid"] = teacherid
        self.teachers_list.append(teacher)

        self.save_teachers_data()

        
    
#6th option in the main menu
    def read_teacher(self):
        if len(self.teachers_list) == 0:
            print("There hasn't been a registeration on the teachers database yet. Please registerate a teacher first and come back later to read the list.")
            return False
    
        sub_teacher_menu()
        epilogi = get_integer_con(1, 3)
        
        
        if int(epilogi) == 1:
            entry = input("Please type any of the elements of the teacher that you want to print: ")
            print_output = []

            for i in range(len(self.teachers_list)):
                if self.teachers_list[i]["name"] == entry or self.teachers_list[i]["surname"] == entry or self.teachers_list[i]["fathersname"] == entry or self.teachers_list[i]["subject"] == entry or self.teachers_list[i]["age"] == int(entry) or self.teachers_list[i]["citizenid"] == int(entry) or self.teachers_list[i]["teacherid"] == int(entry):
                    print_output.append(self.teachers_list[i])

            
            if len(print_output) == 1:
                print(f"Teacher based on the {entry} you typed has this personal info:")
                print(print_output)
            elif len(print_output) > 1:
                print(f"Teachers based on the {entry} you typed has these personal infos:")
                for i in range(len(print_output)):    
                    print(print_output[i])
            else:
                print("Couldnt found a teacher based on the element you typed.")
        
        elif int(epilogi) == 2:
            self.print_teachers_details()

        elif int(epilogi) == 3:
            self.print_teachers_names()

#7th option in the main menu
    def update_teacher(self):
            
        print("1.Search teachers based on surname.\n2.Search teachers based on id.")
        option = get_integer_con(1,2)

        if option == 1:
            while True:
                last_name = get_string("Give the surname of the teacher that you want to update: ")
                my_list = self.search_teacher_by_surname(last_name)
                if len(my_list) > 1:
                    print("There are more than one teacher with this surname on the list.")
                    for id in my_list:
                        for teacher in self.teachers_list:
                            if teacher["teacherid"] == id:
                                print(teacher)
                    
                    id_option = get_integer("Choose one of the above teachers based on threir teacherid: ")
                    while id_option not in my_list:
                        id_option = get_integer("Choose one of the above teachers based on threir teacherid: ")
                    print(f"You chose: {id_option}")

                    for i in range(len(self.teachers_list)):
                        options_available = ["name", "surname", "fathersname", "age", "subject", "citizenid"]
                        if self.teachers_list[i]["teacherid"] == id_option:
                            update_option = get_string("Choose what you want to change in this registration(name, surname, fathersname, age, subject, citizenid): ")
                            while update_option not in options_available:
                                update_option = get_string("Wrong, input. Choose what you want to change in this registration (name, surname, fathersname, age, subject, citizenid): ")
                            self.change_teacher(update_option, i)
                            
                elif len(my_list) == 1:
                    for i in range(len(self.teachers_list)):
                        options_available = ["name", "surname", "fathersname", "age", "subject", "citizenid"]
                        if self.teachers_list[i]["surname"] == last_name:
                            update_option = get_string("Choose what you want to change in this registration (name, surname, fathersname, age, subject, citizenid): ")
                            while update_option not in options_available:
                                update_option = get_string("Wrong input. Choose what you want to change in this registration (name, surname, fathersname, age, subject, citizenid): ")
                            self.change_teacher(update_option, i)

                elif len(my_list) == 0:
                    print("There isn't such a teacher registered in the system. Return back to main menu...")
                    return False
                break
        if option == 2:
            id_option = self.search_teacher_by_id()
            for i in range(len(self.teachers_list)):
                        options_available = ["name", "surname", "fathersname", "age", "subject", "citizenid"]
                        if self.teachers_list[i]["teacherid"] == id_option:
                            update_option = get_string("Choose what you want to change in this registration (name, surname, fathersname, age, subject, citizenid): ")
                            while update_option not in options_available:
                                update_option = get_string("Wrong input. Choose what you want to change in this registration (name, surname, fathersname, age, subject, citizenid): ")
                            self.change_teacher(update_option, i)

#8th option in the main menu
    def delete_teacher(self):

        print("1.Search teachers based on surname.\n2.Search teachers based on id.")
        option = get_integer_con(1,2)

        if option == 1:
            while True:
                last_name = get_string("Give the surname of the teacher that you want to delete: ")
                my_list = self.search_teacher_by_surname(last_name)
                if len(my_list) > 1:
                    print("There are more than one teacher with this surname on the list.")
                    for id in my_list:
                        for teacher in self.teachers_list:
                            if teacher["teacherid"] == id:
                                print(teacher)
                    
                    id_option = get_integer("Choose one of the above teachers based on their teacherid: ")
                    while id_option not in my_list:
                        id_option = get_integer("Choose one of the above teachers based on their teacherid: ")
                    print(f"You chose: {id_option}")
                
                    self.delete_teacher_by_id(id_option)

                elif len(my_list) == 1:
                    for i in range(len(self.teachers_list)):
                        if self.teachers_list[i]["surname"] == last_name:
                            self.teachers_list.pop(i)

                elif len(my_list) == 0:
                    print("There isn't such a teacher registered in the system. Return back to main menu...")
                    return False 
        elif option == 2:
            id_option = self.search_teacher_by_id()
            self.delete_teacher_by_id(id_option)

    def print_teachers_details(self):
        print(f"\n\t\t\tDatabase Καθηγητών:")
        for i in range(len(self.teachers_list)):
            for j in self.teachers_list[i].keys():
                print(f"{j}: {self.teachers_list[i][j]}")
            print("\n")

    def print_teachers_names(self):
        
        for i in range(len(self.teachers_list)):
            print(f"{self.teachers_list[i]["surname"]} {self.teachers_list[i]["name"]} του {self.teachers_list[i]["fathersname"][0]}")

    def delete_teacher_by_id(self, teacher_id):
        for i in range(len(self.teachers_list) - 1):
            if self.teachers_list[i]["teacherid"] == teacher_id:
                self.teachers_list.pop(i)

    
    def search_teacher_by_id(self):
        id_option = get_integer("Δώσε το id του κσθηγητή που θες: ")
        while True:
            for teacher in self.teachers_list:
                if teacher["teacherid"] == id_option:
                    return id_option
            id_option = get_integer("Δεν υπάρχει καθηγητής με αυτό το id στο σύστημα, παρακαλώ εισάγετε ξανά ένα id: ")

    def search_teacher_by_surname(self, last_name):
        id_list = []
        for i in range(len(self.teachers_list)):
            if self.teachers_list[i]["surname"] == last_name:
                id_list.append(self.teachers_list[i]["teacherid"])
        return id_list

    def change_teacher(self, update_option, cnt):

        if update_option == "name":
            change_option = get_string(f"You change the name from {self.teachers_list[cnt]["name"]} to: ")
            self.teachers_list[cnt]["name"] = change_option
        elif update_option == "surname":
            change_option = get_string(f"You change the surname from {self.teachers_list[cnt]["surname"]} to: ")
            self.teachers_list[cnt]["surname"] = change_option
        elif update_option == "fathersname":
            change_option = get_string(f"You change the surname from {self.teachers_list[cnt]["fathersname"]} to: ")
            self.teachers_list[cnt]["fathersname"] = change_option
        elif update_option == "age": 
            change_option = get_integer(f"You change the age from {self.teachers_list[cnt]["age"]} to: ")
            self.teachers_list[cnt]["age"] = change_option
        elif update_option == "subject":
            change_option = get_string(f"You change the subject from {self.teachers_list[cnt]["subject"]} to: ")
            self.teachers_list[cnt]["class"] = change_option
        elif update_option == "citizenid":
            change_option = get_integer(f"You change the citizen id from {self.teachers_list[cnt]["citizenid"]} to:")
            self.teachers_list[cnt]["citizenid"] = change_option

