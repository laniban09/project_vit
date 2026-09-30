from storage import load_data, save_data


def add_student(data):
    student_id = input("Student ID: ").strip()
    if not student_id:
        print("Please enter an ID.")
        return
    if student_id in data["students"]:
        print("That student already exists.")
        return

    name = input("Name: ").strip()
    branch = input("Branch: ").strip()
    if not name or not branch:
        print("Name and branch cannot be empty.")
        return

    data["students"][student_id] = {"name": name, "branch": branch}
    save_data(data)
    print("Student added.")


def show_students(data):
    if not data["students"]:
        print("No students found.")
        return

    for student_id, student in data["students"].items():
        print(student_id, "-", student["name"], "-", student["branch"])


def search_student(data):
    student_id = input("Student ID: ").strip()
    student = data["students"].get(student_id)
    if student:
        print(student_id, "-", student["name"], "-", student["branch"])
    else:
        print("Student not found.")


def delete_student(data):
    student_id = input("Student ID to delete: ").strip()
    if student_id not in data["students"]:
        print("Student not found.")
        return

    answer = input("Delete this student? (y/n): ").lower().strip()
    if answer == "y":
        del data["students"][student_id]
        data["attendance"].pop(student_id, None)
        data["marks"].pop(student_id, None)
        save_data(data)
        print("Student deleted.")


def record_attendance(data):
    student_id = input("Student ID: ").strip()
    if student_id not in data["students"]:
        print("Add the student first.")
        return

    try:
        present = int(input("Classes attended: "))
        total = int(input("Total classes: "))
    except ValueError:
        print("Please enter whole numbers.")
        return

    if total <= 0 or present < 0 or present > total:
        print("Please enter valid attendance numbers.")
        return

    data["attendance"][student_id] = {"present": present, "total": total}
    save_data(data)
    print(f"Attendance: {present / total * 100:.2f}%")


def attendance_report(data):
    for student_id, student in data["students"].items():
        record = data["attendance"].get(student_id)
        if record and record["total"]:
            percentage = record["present"] / record["total"] * 100
        else:
            percentage = 0
        print(f"{student_id} | {student['name']} | {percentage:.2f}%")


def record_marks(data):
    student_id = input("Student ID: ").strip()
    if student_id not in data["students"]:
        print("Add the student first.")
        return

    try:
        count = int(input("Number of subjects: "))
    except ValueError:
        print("Please enter a number.")
        return

    if count <= 0:
        print("Number of subjects should be at least 1.")
        return

    marks = {}
    for _ in range(count):
        subject = input("Subject: ").strip()
        try:
            mark = float(input("Mark (0-100): "))
        except ValueError:
            print("Please enter a valid mark.")
            return

        if not 0 <= mark <= 100:
            print("Mark should be between 0 and 100.")
            return
        marks[subject] = mark

    data["marks"][student_id] = marks
    save_data(data)
    print("Marks saved.")


def performance_report(data):
    for student_id, student in data["students"].items():
        marks = data["marks"].get(student_id, {})
        if not marks:
            print(student_id, "|", student["name"], "| No marks")
            continue

        average = sum(marks.values()) / len(marks)
        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        print(f"{student_id} | {student['name']} | {average:.2f}% | {grade}")


def student_summary(data):
    student_id = input("Student ID: ").strip()
    student = data["students"].get(student_id)
    if not student:
        print("Student not found.")
        return

    record = data["attendance"].get(student_id)
    if record and record["total"]:
        attendance = record["present"] / record["total"] * 100
    else:
        attendance = 0

    print(f"\n{student_id} - {student['name']} - {student['branch']}")
    print(f"Attendance: {attendance:.2f}%")

    marks = data["marks"].get(student_id, {})
    if marks:
        average = sum(marks.values()) / len(marks)
        print("Marks:", marks)
        print(f"Average: {average:.2f}%")
    else:
        print("Marks have not been entered yet.")


def main():
    data = load_data()

    while True:
        print("\nSTUDENT ATTENDANCE AND PERFORMANCE")
        print("1. Add student")
        print("2. List students")
        print("3. Search student")
        print("4. Delete student")
        print("5. Record attendance")
        print("6. Attendance report")
        print("7. Enter marks")
        print("8. Performance report")
        print("9. Student summary")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(data)
        elif choice == "2":
            show_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            delete_student(data)
        elif choice == "5":
            record_attendance(data)
        elif choice == "6":
            attendance_report(data)
        elif choice == "7":
            record_marks(data)
        elif choice == "8":
            performance_report(data)
        elif choice == "9":
            student_summary(data)
        elif choice == "0":
            print("Thank you for using the program.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
