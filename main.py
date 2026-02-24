import json

class Student:
    def __init__(self, name, roll_number, department):
        self.name = name
        self.roll_number = roll_number
        self.department = department

class StudentRecordManagement:
    def __init__(self):
        self.records = []

    def add_student(self, student):
        self.records.append(student)

    def remove_student(self, roll_number):
        self.records = [student for student in self.records if student.roll_number != roll_number]

    def display_students(self):
        for student in self.records:
            print(f'Name: {student.name}, Roll Number: {student.roll_number}, Department: {student.department}')

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([student.__dict__ for student in self.records], f)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                students_data = json.load(f)
                self.records = [Student(**data) for data in students_data]
        except FileNotFoundError:
            print("File not found.")

if __name__ == '__main__':
    manager = StudentRecordManagement()
    while True:
        print('\n1. Add Student\n2. Remove Student\n3. Display Students\n4. Save to File\n5. Load from File\n6. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            name = input('Enter name: ')
            roll_number = input('Enter roll number: ')
            department = input('Enter department: ')
            student = Student(name, roll_number, department)
            manager.add_student(student)
        elif choice == '2':
            roll_number = input('Enter roll number to remove: ')
            manager.remove_student(roll_number)
        elif choice == '3':
            manager.display_students()
        elif choice == '4':
            filename = input('Enter filename to save: ')
            manager.save_to_file(filename)
        elif choice == '5':
            filename = input('Enter filename to load: ')
            manager.load_from_file(filename)
        elif choice == '6':
            break
        else:
            print('Invalid choice!')
