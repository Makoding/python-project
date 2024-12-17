from elegxos import *
from file_management import *

try:
    teachers = load_teachers_data()
except FileNotFoundError:
    save_teachers_data()
    teachers = load_teachers_data()

# 5th option in the main menu
def create_teacher():

    teachers = load_teachers_data()
    teacher = {}

    onoma = get_string("Δώσε το όνομα του καθηγητή προς εγγραφή: ")
    epitheto = get_string("Δώσε το επίθετο του καθηγητή προς εγγραφή: ")
    patronimo = get_string("Δώσε το πατρώνυμο του καθηγητή προς εγγραφή: ")
    
    teacher["name"] = onoma
    teacher["surname"] = epitheto
    teacher["fathersname"] = patronimo
    
    ilikia = get_integer("Δώσε την ηλικία του καθηγητή προς εγγραφή: ")
    teacher["age"] = ilikia

    mathima = get_string("Δώσε το μάθημα του καθηγητή προς εγγραφή: ")
    teacher["subject"] = mathima
    
    id_politi = get_integer("Δώσε τον αριθμό αστυνομικής ταυτότητας, αν υπάρχει: ")
    teacher["citizenid"] = id_politi

    id_teacher = 1000 + len(teachers)
    teacher["teacherid"] = id_teacher
    
    save_teachers_data(teacher)
    print(f"\nΟ καθηγητής {epitheto} {onoma} του {patronimo} ηλικίας {ilikia} χρονών που διδάσκει το μάθημα {mathima} με αστυνομική ταυτότητα υπ΄ αριθμόν {id_politi} και αριθμό μητρόου καθηγητών: {id_teacher} καταχωρήθηκε επιτυχώς στο σύστημα.")
    
    print(f"\n\t\t\tDatabase Καθηγητών:")
    for i in range(len(teachers)):
        for j in teachers[i].keys():
            print(f"{j}: {teachers[i][j]}")
        print("\n")

# 6th option in the main menu        
def read_teacher():
    teachers = load_teachers_data()
    if len(teachers) == 0:
        print("There hasn't been a registeration on the students database yet. Please registerate a student first and come back later to read the list.")
        return False
    
    sub_teacher_menu()
    epilogi = get_integer_con(1, 3)
    
    
    if int(epilogi) == 1:
        entry = input("Πληκτρολόγησε ένα οποιοδήποτε στοιχείο του καθηγητή που θέλεις να εκτυπωθεί: ")
        print_output = []

        for i in range(len(teachers)):
            if teachers[i]["name"] == entry or teachers[i]["surname"] == entry or teachers[i]["fathersname"] == entry or teachers[i]["subject"] == entry or teachers[i]["age"] == int(entry) or teachers[i]["citizenid"] == int(entry) or teachers[i]["teacherid"] == int(entry):
                print_output.append(teachers[i])

        
        if len(print_output) == 1:
            print(f"Ο καθηγητής με βάση το {entry} που πληκτρολογήσατε έχει τα εξής στοιχεία:")
            print(print_output)
        elif len(print_output) > 1:
            print(f"Οι καθηγητές με βάση το {entry} που πληκτρολογήσατε έχουν τα εξής στοιχεία:")
            for i in range(len(print_output)):    
                print(print_output[i])
        else:
            print("Δεν βρέθηκε καθηγητής με βάση το στοιχείο που πληκτρολογήσατε.")
    
    elif int(epilogi) == 2:
        print_teachers_details()

    elif int(epilogi) == 3:
        print_teachers_names()

# 7th option in the main menu
def update_teacher():

    teachers = load_teachers_data()

    print("1.Ψάξε τον καθηγητή με βάση το επίθετο.\n2.Ψάξε το καθηγητή με βάση το id.")
    option = get_integer_con(1,2)

    if option == 1:
        while True:
            last_name = get_string("Δώσε το επίθετο του καθηγητή που θες να ενημερώσεις: ")
            my_list = search_teacher_by_surname(last_name)
            if len(my_list) > 1:
                print("Υπάρχει παραπάνω από ένας καθηγητής με αυτό το επίθετο στη λίστα.")
                for id in my_list:
                    for teacher in teachers:
                        if teacher["teacherid"] == id:
                            print(teacher)
                
                id_option = get_integer("Διάλεξε έναν από τους παραπάνω με βάση το teacherid: ")
                while id_option not in my_list:
                    id_option = get_integer("Διάλεξε έναν από τους παραπάνω με βάση το teacherid: ")
                print(f"Επιλέξατε το {id_option}")

                for i in range(len(teachers)):
                    options_available = ["name", "surname", "fathersname", "age", "subject", "citizenid"]
                    if teachers[i]["teacherid"] == id_option:
                        update_option = get_string("Διάλεξε τι θες να αλλάξεις στην συγκεκριμένη εγγραφή (name, surname, fathersname, age, subject, citizenid): ")
                        while update_option not in options_available:
                            update_option = get_string("Λάθος είσοδος. Διάλεξε τι θες να αλλάξεις στην συγκεκριμένη εγγραφή (name, surname, fathersname, age, subject, citizenid): ")
                        change_teacher(update_option, i)
                        
            elif len(my_list) == 1:
                for i in range(len(teachers)):
                    options_available = ["name", "surname", "fathersname", "age", "subject", "citizenid"]
                    if teachers[i]["surname"] == last_name:
                        update_option = get_string("Διάλεξε τι θες να αλλάξεις στην συγκεκριμένη εγγραφή (name, surname, fathersname, age, subject, citizenid): ")
                        while update_option not in options_available:
                            update_option = get_string("Λάθος είσοδος. Διάλεξε τι θες να αλλάξεις στην συγκεκριμένη εγγραφή (name, surname, fathersname, age, subject, citizenid): ")
                        change_teacher(update_option, i)

            elif len(my_list) == 0:
                print("Δεν υπάρχει τέτοιος καθηγητής καταγεγραμμένος στο σύστημα. Επιστροφή στο αρχικό μενού.")
                return False
            break
    if option == 2:
        id_option = search_teacher_by_id()
        for i in range(len(teachers)):
                    options_available = ["name", "surname", "fathersname", "age", "subject", "citizenid"]
                    if teachers[i]["teacherid"] == id_option:
                        update_option = get_string("Διάλεξε τι θες να αλλάξεις στην συγκεκριμένη εγγραφή (name, surname, fathersname, age, subject, citizenid): ")
                        while update_option not in options_available:
                            update_option = get_string("Λάθος είσοδος. Διάλεξε τι θες να αλλάξεις στην συγκεκριμένη εγγραφή (name, surname, fathersname, age, subject, citizenid): ")
                        change_teacher(update_option, i)

#8th option of the main menu
def delete_teacher():
    teachers = load_teachers_data()

    print("1.Ψάξε τον καθηγητή με βάση το επίθετο.\n2.Ψάξε το καθηγητή με βάση το id.")
    option = get_integer_con(1,2)

    if option == 1:
        while True:
            last_name = get_string("Δώσε το επίθετο του καθηγητή που θες να διαγράψεις: ")
            my_list = search_teacher_by_surname(last_name)
            if len(my_list) > 1:
                print("Υπάρχει παραπάνω από ένας καθηγητής με αυτό το επίθετο στη λίστα.")
                for id in my_list:
                    for teacher in teachers:
                        if teacher["teacherid"] == id:
                            print(teacher)
                
                id_option = get_integer("Διάλεξε έναν από τους παραπάνω με βάση το teacherid: ")
                while id_option not in my_list:
                    id_option = get_integer("Διάλεξε έναν από τους παραπάνω με βάση το teacherid: ")
                print(f"Επιλέξατε το {id_option}")
            
                delete_teacher_by_id(id_option)

            elif len(my_list) == 1:
                for i in range(len(teachers)):
                    if teachers[i]["surname"] == last_name:
                        teachers.pop(i)

            elif len(my_list) == 0:
                print("Δεν υπάρχει τέτοιος καθηγητής καταγεγραμμένος στο σύστημα. Επιστροφή στο αρχικό μενού.")
                return False 
    elif option == 2:
        id_option = search_teacher_by_id()
        delete_teacher_by_id(id_option)

def sub_teacher_menu():

    print("="*60)
    print("MΕΝΟΥ ΕΠΙΛΟΓΩΝ ΕΚΤΥΠΩΣΗΣ")
    print("="*60)

    print("\n1. Eκτύπωση Καθηγητή\n2. Εκτύπωση όλων των καθηγητών (αναλυτική)\n3. Εκτύπωση όλων των καθηγητών (μόνο ονόματα)")
 
def print_teachers_details():
    teachers = load_teachers_data()
    print(f"\n\t\t\tDatabase Καθηγητών:")
    for i in range(len(teachers)):
        for j in teachers[i].keys():
            print(f"{j}: {teachers[i][j]}")
        print("\n")

def print_teachers_names():
    teachers = load_teachers_data()
    for i in range(len(teachers)):
        print(f"{teachers[i]["surname"]} {teachers[i]["name"]} του {teachers[i]["fathersname"][0]}")

def search_teacher_by_surname(eponymo):
    teachers = load_teachers_data()
    id_list = []
    for i in range(len(teachers)):
        if teachers[i]["surname"] == eponymo:
            id_list.append(teachers[i]["teacherid"])
    
    return id_list

def search_teacher_by_id():
    teachers = load_teachers_data()
    id_option = get_integer("Δώσε το id του κσθηγητή που θες: ")
    while True:
        for teacher in teachers:
            if teacher["teacherid"] == id_option:
                return id_option
        id_option = get_integer("Δεν υπάρχει καθηγητής με αυτό το id στο σύστημα, παρακαλώ εισάγετε ξανά ένα id: ")

def delete_teacher_by_id(teacher_id):
    teachers = load_teachers_data()
    for i in range(len(teachers) - 1):
        if teachers[i]["teacherid"] == teacher_id:
            teachers.pop(i)
    alter_teachers_data(teachers)

def change_teacher(update_option, cnt):

    teachers = load_teachers_data()

    if update_option == "name":
        change_option = get_string(f"Αλλάζεις το όνομα από {teachers[cnt]["name"]} σε: ")
        teachers[cnt]["name"] = change_option
    elif update_option == "surname":
        change_option = get_string(f"Αλλάζεις το επίθετο από {teachers[cnt]["surname"]} σε: ")
        teachers[cnt]["surname"] = change_option
    elif update_option == "fathersname":
        change_option = get_string(f"Αλλάζεις το πατρόνυμο από {teachers[cnt]["fathersname"]} σε: ")
        teachers[cnt]["fathersname"] = change_option
    elif update_option == "age": 
        change_option = get_integer(f"Αλλάζεις την ηλικία από {teachers[cnt]["age"]} σε: ")
        teachers[cnt]["age"] = change_option
    elif update_option == "subject":
        change_option = get_string(f"Αλλάζεις τo μάθημα από {teachers[cnt]["subject"]} σε: ")
        teachers[cnt]["class"] = change_option
    elif update_option == "citizenid":
        change_option = get_integer(f"Αλλάζεις τον αριθμό ταυτότητας από {teachers[cnt]["citizenid"]} σε: ")
        teachers[cnt]["citizenid"] = change_option

    alter_teachers_data(teachers)