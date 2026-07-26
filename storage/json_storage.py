import json

FILE_PATH = "data/students.json"


def load_students():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_students(students):
    with open(FILE_PATH, "w") as file:
        json.dump(students, file, indent=4)


def add_student(student):
    students = load_students()

    # Check for duplicate Student ID
    for existing_student in students:
        if existing_student['id'] == student['id']:
            return False

    students.append(student)
    save_students(students)
    return True

def get_student_by_id(student_id):
    students = load_students()

    for student in students:
        if student["id"] == student_id:
            return student
    return None


def delete_student(student_id):
    students = load_students()

    updated_students = []

    deleted = False

    for student in students:
        if student["id"] != student_id:
            updated_students.append(student)
        else:
            deleted = True

    save_students(updated_students)
    return deleted


def update_student(student_id, updated_data):
    students = load_students()

    for index, student in enumerate(students):
        if student["id"] == student_id:
            students[index] = updated_data
            save_students(students)
            return True

    return False