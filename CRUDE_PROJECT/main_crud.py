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

    print("\n\n1.\tΔημιουργία Εγγραφής Μαθητών")
    print("\n2.\tΕκτύπωση Εγγραφών Μαθητών")
    print("\n3\tΕνημέρωση Εγγραφής Μαθητών")
    print("\n4.\tΔιαγραφή Εγγραφής Μαθητών")
    print("\n5.\tΔημιουργία Εγγραφής Καθηγητών")
    print("\n6.\tΕκτύπωση Εγγραφών Καθηγητών")
    print("\n7.\tΕνημέρωση Εγγραφής Καθηγητών")
    print("\n8.\tΔιαγραφή Εγγραφής Καθηγητών")
    
    print("\n9.\tΈξοδος")


# 1st option in the main menu
def create_student():
    students = load_students_data()
    student = {}

    onoma = get_string("Δώσε το όνομα του μαθητή προς εγγραφή: ")
    epitheto = get_string("Δώσε το επίθετο του μαθητή προς εγγραφή: ")
    patronimo = get_string("Δώσε το πατρώνυμο του μαθητή προς εγγραφή: ")
    """while True:
        for i in range(len(students)):
            if students[i]["name"] == onoma and students[i]["surname"] == epitheto and students[i]["fathersname"] == patronimo:
                epistrofi = input("Υπάρχει ήδη μαθητής καταχωρημένος στο σύστημα με αυτά τα στοιχεία, θέλετε να συνεχίσετε; Yes για ναι. ")
                if epistrofi == "Yes" or epistrofi == "yes":
                    break
                else:
                    return None
        break"""
    student["name"] = onoma
    student["surname"] = epitheto
    student["fathersname"] = patronimo
    
    ilikia = get_integer("Δώσε την ηλικία του μαθητή προς εγγραφή: ")
    student["age"] = ilikia

    taksi = get_integer("Δώσε την τάξη του μαθητή προς εγγραφή: ")
    student["class"] = taksi
    
    id_politi = get_integer("Δώσε τον αριθμό αστυνομικής ταυτότητας, αν υπάρχει: ")
    student["citizenid"] = id_politi
    print(students)
    id_mathiti = 1000 + len(students)
    student["studentid"] = id_mathiti
    
    save_students_data(student)
    students = load_students_data()
    print(f"\nΟ μαθητής {epitheto} {onoma} του {patronimo} ηλικίας {ilikia} χρονών που φοιτεί στην {taksi}η με αστυνομική ταυτότητα υπ΄ αριθμόν {id_politi} και μαθητικό αριθμό μητρόου {id_mathiti} καταχωρήθηκε επιτυχώς στο σύστημα.")
    
    print(f"\n\t\t\tDatabase Μαθητών:")
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
        entry = input("Πληκτρολόγησε ένα οποιοδήποτε στοιχείο του μαθήτη που θέλεις να εκτυπωθεί: ")
        print_output = []

        for i in range(len(students)):
            if students[i]["name"] == entry or students[i]["surname"] == entry or students[i]["fathersname"] == entry or students[i]["age"] == int(entry) or int(students[i]["class"]) == int(entry) or students[i]["citizenid"] == int(entry) or students[i]["studentid"] == int(entry):
                print_output.append(students[i])

        
        if len(print_output) == 1:
            print(f"Ο μαθητής με βάση το {entry} που πληκτρολογήσατε έχει τα εξής στοιχεία:")
            print(print_output)
        elif len(print_output) > 1:
            print(f"Οι μαθητές με βάση το {entry} που πληκτρολογήσατε έχουν τα εξής στοιχεία:")
            for i in range(len(print_output)):    
                print(print_output[i])
        else:
            print("Δεν βρέθηκε μαθητής με βάση το στοιχείο που πληκτρολογήσατε.")
    
    elif int(epilogi) == 2:
        print_students_details()

    elif int(epilogi) == 3:
        print_students_names()

# 3rd option in the main menu
def update_student():
    students = load_students_data()
    print("1.Ψάξε τον μαθητή με βάση το επίθετο.\n2.Ψάξε το μαθητή με βάση το id.")
    option = get_integer_con(1,2)

    if option == 1:
        while True:
            last_name = get_string("Δώσε το επίθετο του μαθητή που θες να ενημερώσεις: ")
            my_list = search_student_by_surname(last_name)
            if len(my_list) > 1:
                print("Υπάρχει παραπάνω από ένας μαθητής με αυτό το επίθετο στη λίστα.")
                for id in my_list:
                    for student in students:
                        if student["studentid"] == id:
                            print(student)
                
                id_option = get_integer("Διάλεξε έναν από τους παραπάνω με βάση το studentid: ")
                while id_option not in my_list:
                    id_option = get_integer("Διάλεξε έναν από τους παραπάνω με βάση το studentid: ")
                print(f"Επιλέξατε το {id_option}")                          

                for i in range(len(students)):
                    options_available = ["name", "surname", "fathersname", "age", "class", "citizenid"]
                    if students[i]["studentid"] == id_option:
                        update_option = get_string("Διάλεξε τι θες να αλλάξεις στην συγκεκριμένη εγγραφή (name, surname, fathersname, age, class, citizenid): ")
                        while update_option not in options_available:
                            update_option = get_string("Λάθος είσοδος. Διάλεξε τι θες να αλλάξεις στην συγκεκριμένη εγγραφή (name, surname, fathersname, age, class, citizenid): ")
                        change_student(update_option, i)

            elif len(my_list) == 1:
                for i in range(len(students)):
                    options_available = ["name", "surname", "fathersname", "age", "class", "citizenid"]
                    if students[i]["surname"] == last_name:
                        update_option = get_string("Διάλεξε τι θες να αλλάξεις στην συγκεκριμένη εγγραφή (name, surname, fathersname, age, class, citizenid): ")
                        while update_option not in options_available:
                            update_option = get_string("Λάθος είσοδος. Διάλεξε τι θες να αλλάξεις στην συγκεκριμένη εγγραφή (name, surname, fathersname, age, class, citizenid): ")
                        change_student(update_option, i)

                        
            elif len(my_list) == 0:
                print("Δεν υπάρχει τέτοιος μαθητής καταγεγραμμένος στο σύστημα. Επιστροφή στο αρχικό μενού.")
                return False
            break
    if option == 2:
        id_option = search_student_by_id()
        for i in range(len(students)):
                    options_available = ["name", "surname", "fathersname", "age", "class", "citizenid"]
                    if students[i]["studentid"] == id_option:
                        update_option = get_string("Διάλεξε τι θες να αλλάξεις στην συγκεκριμένη εγγραφή (name, surname, fathersname, age, class, citizenid): ")
                        while update_option not in options_available:
                            update_option = get_string("Λάθος είσοδος. Διάλεξε τι θες να αλλάξεις στην συγκεκριμένη εγγραφή (name, surname, fathersname, age, class, citizenid): ")
                        change_student(update_option, i)



#4trh option of the main menu
def delete_student():
    students = load_students_data()
    print("1.Ψάξε τον μαθητή με βάση το επίθετο.\n2.Ψάξε το μαθητή με βάση το id.")
    option = get_integer_con(1,2)

    if option == 1:
        while True:
            last_name = get_string("Δώσε το επίθετο του μαθητή που θες να διαγράψεις: ")
            my_list = search_student_by_surname(last_name)
            if len(my_list) > 1:
                print("Υπάρχει παραπάνω από ένας μαθητής με αυτό το επίθετο στη λίστα.")
                for id in my_list:
                    for student in students:
                        if student["studentid"] == id:
                            print(student)
                
                id_option = get_integer("Διάλεξε έναν από τους παραπάνω με βάση το studentid: ")
                while id_option not in my_list:
                    id_option = get_integer("Διάλεξε έναν από τους παραπάνω με βάση το studentid: ")
                print(f"Επιλέξατε το {id_option}")
            
                delete_student_by_id(id_option)

            elif len(my_list) == 1:
                for i in range(len(students)):
                    if students[i]["surname"] == last_name:
                        students.pop(i)

            elif len(my_list) == 0:
                print("Δεν υπάρχει τέτοιος μαθητής καταγεγραμμένος στο σύστημα. Επιστροφή στο αρχικό μενού.")
                return False 
    elif option == 2:
        id_option = search_student_by_id()
        delete_student_by_id(id_option)

def sub_menu():

    print("="*60)
    print("MΕΝΟΥ ΕΠΙΛΟΓΩΝ ΕΚΤΥΠΩΣΗΣ")
    print("="*60)

    print("\n1. Eκτύπωση Μαθητή\n2. Εκτύπωση όλων των μαθητών (αναλυτική)\n3. Εκτύπωση όλων των μαθητών (μόνο ονόματα)")

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
        print(f"{students[i]["surname"]} {students[i]["name"]} του {students[i]["fathersname"][0]}")
    

def next_id():
    students = load_students_data()
    if len(students) > 0:
        return f"Το επόμενο διαθέσιμο id είναι το: {students[len(students)-1]["studentid"]+1}"
    else:
        return f"Το επόμενο διαθέσιμο id είναι το: {1000}"
    
def search_student_by_surname(eponymo):
    students = load_students_data()
    id_list = []
    for i in range(len(students)):
        if students[i]["surname"] == eponymo:
            id_list.append(students[i]["studentid"])
    
    return id_list

def search_student_by_id():
    students = load_students_data()
    id_option = get_integer("Δώσε το id του μαθήτη που θες: ")
    while True:
        for student in students:
            if student["studentid"] == id_option:
                return id_option
        id_option = get_integer("Δεν υπάρχει μαθητής με αυτό το id στο σύατημα, παρακαλώ εισάγετε ξανά ένα id: ")

def delete_student_by_id(student_id):
    students = load_students_data()
    for i in range(len(students) - 1):
        if students[i]["studentid"] == student_id:
            students.pop(i)

def change_student(update_option,cnt):
    students = load_students_data()
                        
    if update_option == "name":
        change_option = get_string(f"Αλλάζεις το όνομα από {students[cnt]["name"]} σε: ")
        students[cnt]["name"] = change_option
    elif update_option == "surname":
        change_option = get_string(f"Αλλάζεις το επίθετο από {students[cnt]["surname"]} σε: ")
        students[cnt]["surname"] = change_option
    elif update_option == "fathersname":
        change_option = get_string(f"Αλλάζεις το πατρόνυμο από {students[cnt]["fathersname"]} σε: ")
        students[cnt]["fathersname"] = change_option
    elif update_option == "age": 
        change_option = get_integer(f"Αλλάζεις την ηλικία από {students[cnt]["age"]} σε: ")
        students[cnt]["age"] = change_option
    elif update_option == "class":
        change_option = get_integer(f"Αλλάζεις την τάξη από {students[cnt]["class"]} σε: ")
        students[cnt]["class"] = change_option
    elif update_option == "citizenid":
        change_option = get_integer(f"Αλλάζεις τον αριθμό ταυτότητας από {students[cnt]["citizenid"]} σε: ")
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