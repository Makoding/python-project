import json


def save_students_data(input_data = {}):
    if len(input_data)>0:
        new_data = load_students_data()
        new_data.append(input_data)
    try:
        with open("students_data.json", "w") as f:
            students = json.dump(new_data,f)
    except :
        with open("students_data.json", "w") as f:
            students = json.dump([],f)

def load_students_data():
    with open("students_data.json", "r") as f:
        students = json.load(f)
    return students

def alter_students_data(students_list):
    with open("students_data.json", "w") as f:
        students_list = json.dump(students_list,f)


def save_teachers_data(input_data = {}):
    if len(input_data) >0:
        new_data = load_teachers_data()
        new_data.append(input_data)
    try:
        with open("teachers_data.json", "w") as f:
            teachers = json.dump(new_data,f)
    except:
        with open("teachers_data.json", "w") as f:
            teachers = json.dump([],f)

def load_teachers_data():
    with open("teachers_data.json", "r") as f:
        teachers = json.load(f)
    return teachers

def alter_teachers_data(teachers_list):
    with open("teachers_data.json", "w") as f:
        teachers_list = json.dump(teachers_list,f)