import csv
import os
from datetime import datetime

class SchoolManagementSystem:
    def __init__(self, filename='students.csv'):
        self.filename = filename
        if not os.path.isfile(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'Name', 'Age', 'Grade', 'Address', 'Phone', 'Email', 'Parent/Guardian Name'])

    def add_student(self, student_id, name, age, grade, address, phone, email, guardian_name):
        if not self.is_valid_age(age):
            print("Invalid age. Age must be between 5 and 100.")
            return
        
        if not self.is_valid_grade(grade):
            print("Invalid grade. Grade must be one of: A, B, C, D, F.")
            return

        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student_id, name, age, grade.upper(), address, phone, email, guardian_name])
        print(f"Student {name} added successfully.")

    def view_students(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                header = next(reader, None)  # skip header
                students = list(reader)

                if not students:
                    print("No students to display.")
                    return

                for row in students:
                    if row:
                        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}, "
                              f"Address: {row[4]}, Phone: {row[5]}, Email: {row[6]}, Guardian: {row[7]}")
        except FileNotFoundError:
            print(f"The file {self.filename} does not exist. Please add students first.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_student(self, student_id):
        students = []
        found = False
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                header = next(reader)
                students.append(header)
                for row in reader:
                    if row[0] != student_id:
                        students.append(row)
                    else:
                        found = True
            if found:
                with open(self.filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(students)
                print(f"Student with ID {student_id} deleted successfully.")
            else:
                print(f"Student with ID {student_id} not found.")
        except FileNotFoundError:
            print(f"The file {self.filename} does not exist. Please add students first.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def update_student(self, student_id, new_name=None, new_age=None, new_grade=None,
                       new_address=None, new_phone=None, new_email=None, new_guardian=None):
        students = []
        found = False
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                header = next(reader)
                students.append(header)
                for row in reader:
                    if row[0] == student_id:
                        found = True
                        row[1] = new_name if new_name else row[1]
                        row[2] = new_age if new_age else row[2]
                        row[3] = new_grade if new_grade else row[3]
                        row[4] = new_address if new_address else row[4]
                        row[5] = new_phone if new_phone else row[5]
                        row[6] = new_email if new_email else row[6]
                        row[7] = new_guardian if new_guardian else row[7]
                    students.append(row)

            if found:
                with open(self.filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(students)
                print(f"Student with ID {student_id} updated successfully.")
            else:
                print(f"Student with ID {student_id} not found.")
        except FileNotFoundError:
            print(f"The file {self.filename} does not exist. Please add students first.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def search_student(self, search_term):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                header = next(reader, None)
                found = False
                for row in reader:
                    if (search_term.lower() in row[0].lower() or
                        search_term.lower() in row[1].lower()):
                        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}, "
                              f"Address: {row[4]}, Phone: {row[5]}, Email: {row[6]}, Guardian: {row[7]}")
                        found = True

                if not found:
                    print(f"No student found with the term '{search_term}'.")
        except FileNotFoundError:
            print(f"The file {self.filename} does not exist. Please add students first.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def sort_students(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                header = next(reader, None)
                students = list(reader)

                if not students:
                    print("No students to sort.")
                    return

                students.sort(key=lambda x: x[3])  # sort by Grade

                for row in students:
                    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}, "
                          f"Address: {row[4]}, Phone: {row[5]}, Email: {row[6]}, Guardian: {row[7]}")
        except FileNotFoundError:
            print(f"The file {self.filename} does not exist. Please add students first.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def export_to_txt(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                students = list(reader)

            if len(students) <= 1:  # only header present
                print("No student data to export.")
                return

            with open('students.txt', mode='w') as file:
                for row in students:
                    file.write(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}, "
                               f"Address: {row[4]}, Phone: {row[5]}, Email: {row[6]}, Guardian: {row[7]}\n")
            print("Student data exported to students.txt.")
        except FileNotFoundError:
            print(f"The file {self.filename} does not exist. Please add students first.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def student_count(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader, None)  # skip header
                count = sum(1 for row in reader)
            print(f"Total number of students: {count}")
        except FileNotFoundError:
            print(f"The file {self.filename} does not exist. Please add students first.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def is_valid_age(self, age):
        try:
            age = int(age)
            return 5 <= age <= 100
        except ValueError:
            return False

    def is_valid_grade(self, grade):
        return grade.upper() in ['A', 'B', 'C', 'D', 'F']

def main():
    sms = SchoolManagementSystem()
    
    while True:
        print("\nSchool Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Update Student")
        print("5. Search Student")
        print("6. Sort Students by Grade")
        print("7. Export Students to Text File")
        print("8. Total Student Count")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = input("Enter Student Age: ")
            grade = input("Enter Student Grade: ")
            address = input("Enter Student Address: ")
            phone = input("Enter Student Phone: ")
            email = input("Enter Student Email: ")
            guardian_name = input("Enter Guardian Name: ")
            sms.add_student(student_id, name, age, grade, address, phone, email, guardian_name)
        elif choice == '2':
            sms.view_students()
        elif choice == '3':
            student_id = input("Enter Student ID to delete: ")
            sms.delete_student(student_id)
        elif choice == '4':
            student_id = input("Enter Student ID to update: ")
            new_name = input("Enter new name (leave blank to keep current): ")
            new_age = input("Enter new age (leave blank to keep current): ")
            new_grade = input("Enter new grade (leave blank to keep current): ")
            new_address = input("Enter new address (leave blank to keep current): ")
            new_phone = input("Enter new phone (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            new_guardian = input("Enter new guardian name (leave blank to keep current): ")
            sms.update_student(student_id, new_name, new_age, new_grade, new_address, new_phone, new_email, new_guardian)
        elif choice == '5':
            search_term = input("Enter student ID or name to search: ")
            sms.search_student(search_term)
        elif choice == '6':
            sms.sort_students()
        elif choice == '7':
            sms.export_to_txt()
        elif choice == '8':
            sms.student_count()
        elif choice == '9':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
