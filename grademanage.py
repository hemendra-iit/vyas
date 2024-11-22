student_grade = {}

def add_student(name, grade):
    # Add the student to the dictionary
    student_grade[name] = grade
    print(f"Added {name} with a grade of {grade}.")

def update_student(name, grade):
    # Check if the student exists before updating
    if name in student_grade:
        student_grade[name] = grade
        print(f"{name}'s grade has been updated to {grade}.")
    else:
        print(f"{name} is not found!")

def delete_student(name):
    # Delete the student if they exist in the dictionary
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been successfully deleted.")
    else:
        print(f"{name} is not found!")

def display_all_students():
    # Display all students and their grades
    if student_grade:
        print("\nStudent Grades:")
        for name, grade in student_grade.items():
            print(f" - {name}: {grade}")
    else:
        print("No students found.")

def main():
    while True:
        print("\nStudent Grades Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            name = input("Enter student name: ").strip()
            try:
                grade = int(input("Enter student grade: "))
                add_student(name, grade)
            except ValueError:
                print("Invalid grade! Please enter an integer.")
        elif choice == 2:
            name = input("Enter student name: ").strip()
            try:
                grade = int(input("Enter new grade: "))
                update_student(name, grade)
            except ValueError:
                print("Invalid grade! Please enter an integer.")
        elif choice == 3:
            name = input("Enter student name: ").strip()
            delete_student(name)
        elif choice == 4:
            display_all_students()
        elif choice == 5:
            print("Closing the program...")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
