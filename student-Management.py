import csv
import os


# Student class
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }


# Manager class
class StudentManager:
    def __init__(self, filename="students.csv"):
        self.filename = filename
        self.students = []
        self.load_students()

    # Load students from CSV file
    def load_students(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student(
                    row["id"],
                    row["name"],
                    row["grade"]
                )
                self.students.append(student)

    # Save students to CSV file
    def save_students(self):
        with open(self.filename, "w", newline="") as file:
            fieldnames = ["id", "name", "grade"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for student in self.students:
                writer.writerow(student.to_dict())

    # Check whether ID already exists
    def id_exists(self, student_id):
        return any(
            student.student_id == student_id
            for student in self.students
        )

    # Add student
    def add_student(self, student):
        if self.id_exists(student.student_id):
            print("\nError: Student ID already exists.")
            return

        self.students.append(student)
        self.save_students()
        print("\nStudent added successfully.")

    # Update student
    def update_student(self, student_id, name, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.name = name
                student.grade = grade

                self.save_students()
                print("\nStudent updated successfully.")
                return

        print("\nError: Student not found.")

    # Delete student
    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_students()

                print("\nStudent deleted successfully.")
                return

        print("\nError: Student not found.")

    # List students
    def list_students(self):
        if not self.students:
            print("\nNo student records found.")
            return

        print("\n" + "=" * 50)
        print(f"{'ID':<15}{'Name':<20}{'Grade':<15}")
        print("=" * 50)

        for student in self.students:
            print(
                f"{student.student_id:<15}"
                f"{student.name:<20}"
                f"{student.grade:<15}"
            )

        print("=" * 50)

    # Search student
    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print("\nStudent Found")
                print("-" * 30)
                print(f"ID    : {student.student_id}")
                print(f"Name  : {student.name}")
                print(f"Grade : {student.grade}")
                print("-" * 30)
                return

        print("\nError: Student not found.")


# Input validation functions
def get_student_id():
    while True:
        student_id = input("Enter student ID: ").strip()

        if student_id:
            return student_id

        print("ID cannot be empty.")


def get_name():
    while True:
        name = input("Enter student name: ").strip()

        if name:
            return name

        print("Name cannot be empty.")


def get_grade():
    while True:
        grade = input("Enter student grade: ").strip()

        if grade:
            return grade

        print("Grade cannot be empty.")


# Main program
def main():
    manager = StudentManager()

    while True:
        print("\n")
        print("=" * 50)
        print("       STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Search Student")
        print("6. Exit")
        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_id = get_student_id()
            name = get_name()
            grade = get_grade()

            student = Student(student_id, name, grade)
            manager.add_student(student)

        elif choice == "2":
            student_id = get_student_id()
            name = get_name()
            grade = get_grade()

            manager.update_student(student_id, name, grade)

        elif choice == "3":
            student_id = get_student_id()
            manager.delete_student(student_id)

        elif choice == "4":
            manager.list_students()

        elif choice == "5":
            student_id = get_student_id()
            manager.search_student(student_id)

        elif choice == "6":
            print("\nThank you for using Student Management System!")
            break

        else:
            print("\nInvalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()