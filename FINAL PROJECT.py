# Student Marks Management System (Basic Python)

students = []

def add_student():
    name = input("Enter student name: ")
    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter mark {i}: "))
        marks.append(mark)
    student = {"name": name, "marks": marks}
    students.append(student)
    print("Student added successfully.\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    print("\n--- Student Records ---")
    for idx, student in enumerate(students, 1):
        print(f"{idx}. {student['name']} - Marks: {student['marks']}")
    print()

def search_student():
    name = input("Enter student name to search: ")
    found = False
    for student in students:
        if student['name'].lower() == name.lower():
            print(f"Found: {student['name']} - Marks: {student['marks']}\n")
            found = True
            break
    if not found:
        print("Student not found.\n")

def delete_student():
    name = input("Enter student name to delete: ")
    for i, student in enumerate(students):
        if student['name'].lower() == name.lower():
            del students[i]
            print("Student deleted successfully.\n")
            return
    print("Student not found.\n")

def show_statistics():
    if not students:
        print("No data to show statistics.\n")
        return

    total_marks = []
    for student in students:
        total = sum(student['marks'])
        total_marks.append(total)

    print("📊 Statistics:")
    print(f"Total Students: {len(students)}")
    print(f"Average Total Marks: {sum(total_marks)/len(students):.2f}")
    print(f"Highest Marks: {max(total_marks)}")
    print(f"Lowest Marks: {min(total_marks)}\n")

def menu():
    while True:
        print("=== Student Marks Management ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Show Statistics")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            show_statistics()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run the program
menu()
