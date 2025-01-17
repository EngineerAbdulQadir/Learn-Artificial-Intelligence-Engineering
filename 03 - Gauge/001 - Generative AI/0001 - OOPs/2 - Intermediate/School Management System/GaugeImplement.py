# prompt: read above cell and make a new function of add course

import csv
from datetime import datetime
# # Education Trust Nasra School - School Management System

# ----------------------------- DATABASES -----------------------------
students_db = {
    "001": {"Name": "Alice", "Courses": [], "Grades": {}, "Marks": {}, "Fees Paid": 0, "Course Completion": {}},
    "002": {"Name": "Bob",   "Courses": [], "Grades": {}, "Marks": {}, "Fees Paid": 0, "Course Completion": {}},
}

attendance_db = {
    "001": {},
    "002": {},
}

fee_structure = {
    "Course A": 3000,
    "Course B": 2500,
}

# ----------------------------- STUDENT MANAGEMENT -----------------------------
def add_student():
    """Add a new student to the database."""
    roll_no = input("Enter Roll Number: ").strip()
    name = input("Enter Student Name: ").strip()
    if roll_no in students_db:
        print(f"A student with Roll Number {roll_no} already exists.")
        return
    students_db[roll_no] = {
        "Name": name,
        "Courses": [],
        "Grades": {},
        "Marks": {},
        "Fees Paid": 0,
        "Course Completion": {}
    }
    print(f"Student '{name}' added with Roll Number '{roll_no}'.")

def update_student():
    """Update an existing student's name."""
    roll_no = input("Enter Roll Number: ").strip()
    if roll_no not in students_db:
        print("Student not found!")
        return
    new_name = input("Enter new name: ").strip()
    students_db[roll_no]['Name'] = new_name
    print(f"Student with Roll Number '{roll_no}' updated to '{new_name}'.")

def delete_student():
    """Remove a student from the database."""
    roll_no = input("Enter Roll Number: ").strip()
    if roll_no in students_db:
        del students_db[roll_no]
        # Also remove attendance record if present
        if roll_no in attendance_db:
            del attendance_db[roll_no]
        print(f"Student with Roll Number '{roll_no}' deleted.")
    else:
        print("Student not found!")

def view_students():
    """Display all students in the database."""
    print("\nList of Students:")
    if not students_db:
        print("No students found.")
        return
    for roll_no, details in students_db.items():
        print(f"Roll No: {roll_no}, Name: {details['Name']}")

def search_student():
    """Search for a student by roll number or name."""
    search_term = input("Enter Roll Number or Name to search: ").strip()
    found = False
    for roll_no, details in students_db.items():
        if search_term == roll_no or search_term.lower() == details['Name'].lower():
            print(f"Found: Roll No: {roll_no}, Name: {details['Name']}")
            found = True
    if not found:
        print("No matching student found.")

# ----------------------------- COURSE ENROLLMENT -----------------------------
def enroll_course():
    """Enroll a student in a course if it's in the fee structure."""
    roll_no = input("Enter Roll Number: ").strip()
    if roll_no not in students_db:
        print("Student not found!")
        return
    course_name = input("Enter Course Name: ").strip()
    if course_name in fee_structure:
        students_db[roll_no]['Courses'].append(course_name)
        print(f"{students_db[roll_no]['Name']} enrolled in '{course_name}'.")
    else:
        print("Course not found in fee structure.")

def remove_course():
    """Unenroll a student from a specific course."""
    roll_no = input("Enter Roll Number: ").strip()
    if roll_no not in students_db:
        print("Student not found!")
        return
    course_name = input("Enter Course Name to Remove: ").strip()
    if course_name in students_db[roll_no]['Courses']:
        students_db[roll_no]['Courses'].remove(course_name)
        print(f"'{course_name}' removed from {students_db[roll_no]['Name']}'s courses.")
    else:
        print(f"{students_db[roll_no]['Name']} is not enrolled in '{course_name}'.")

def edit_course():
    """Replace a student's old course with a new one."""
    roll_no = input("Enter Roll Number: ").strip()
    if roll_no not in students_db:
        print("Student not found!")
        return
    old_course_name = input("Enter Current Course Name: ").strip()
    if old_course_name in students_db[roll_no]['Courses']:
        new_course_name = input("Enter New Course Name: ").strip()
        index = students_db[roll_no]['Courses'].index(old_course_name)
        students_db[roll_no]['Courses'][index] = new_course_name
        print(f"'{old_course_name}' changed to '{new_course_name}' for {students_db[roll_no]['Name']}.")
    else:
        print(f"{students_db[roll_no]['Name']} is not enrolled in '{old_course_name}'.")

def view_courses():
    """Display all courses a student is currently enrolled in."""
    roll_no = input("Enter Roll Number: ").strip()
    if roll_no not in students_db:
        print("Student not found!")
        return
    courses = students_db[roll_no]['Courses']
    if courses:
        print(f"Courses enrolled by {students_db[roll_no]['Name']}: {', '.join(courses)}")
    else:
        print(f"{students_db[roll_no]['Name']} is not enrolled in any courses.")

def add_course():
    """Add a new course to the fee structure."""
    course_name = input("Enter Course Name: ").strip()
    if course_name in fee_structure:
        print(f"Course '{course_name}' already exists.")
        return
    try:
        fee = int(input("Enter Course Fee: ").strip())
        if fee < 0:
            print("Fee cannot be negative.")
            return
        fee_structure[course_name] = fee
        print(f"Course '{course_name}' added with fee {fee}.")
    except ValueError:
        print("Invalid fee amount. Please enter an integer.")

# ----------------------------- ATTENDANCE MANAGEMENT -----------------------------
def mark_attendance():
    """Mark a student's attendance for a given date."""
    roll_no = input("Enter Roll Number: ").strip()
    if roll_no not in students_db:
        print("Student not found!")
        return
    date = input("Enter Date (YYYY-MM-DD): ").strip()
    status = input("Enter Status (Present/Absent): ").strip().capitalize()
    attendance_db.setdefault(roll_no, {})[date] = status
    print(f"Attendance marked for {students_db[roll_no]['Name']} on {date} as {status}.")

def view_attendance():
    """View a student's attendance record."""
    roll_no = input("Enter Roll Number: ").strip()
    if roll_no not in attendance_db:
        print("No attendance record found for this student.")
        return
    print(f"\nAttendance for {students_db[roll_no]['Name']}:")
    for date, status in attendance_db[roll_no].items():
        print(f"{date}: {status}")

# ----------------------------- GRADE & MARK MANAGEMENT -----------------------------
def assign_marks_and_grade():
    """
    Assign marks (out of 100) and a grade (A, B, C, D, F) to a student
    for a specific course. Also mark the course as incomplete initially.
    """
    roll_no = input("Enter Roll Number: ").strip()
    if roll_no not in students_db:
        print("Student not found!")
        return
    course_name = input("Enter Course Name: ").strip()
    marks = input("Enter Marks (out of 100): ").strip()
    grade = input("Enter Grade (A, B, C, D, F): ").strip().upper()

    students_db[roll_no]['Marks'][course_name] = marks
    students_db[roll_no]['Grades'][course_name] = grade
    students_db[roll_no]['Course Completion'][course_name] = False  # Mark incomplete initially
    print(f"Marks {marks} and Grade {grade} assigned to {students_db[roll_no]['Name']} for '{course_name}'.")

def view_marks_and_grades():
    """View the marks and grades for each course a student is enrolled in."""
    roll_no = input("Enter Roll Number: ").strip()
    if roll_no not in students_db:
        print("Student not found!")
        return

    student_name = students_db[roll_no]['Name']
    courses = students_db[roll_no]['Courses']
    print(f"\nMarks and Grades for {student_name}:")
    if not courses:
        print("No courses enrolled.")
        return

    for course in courses:
        marks = students_db[roll_no]['Marks'].get(course, 'No marks assigned')
        grade = students_db[roll_no]['Grades'].get(course, 'No grade assigned')
        print(f"{course}: Marks = {marks}, Grade = {grade}")

# ----------------------------- FEE MANAGEMENT -----------------------------
def pay_fees():
    """Pay the fee for a specific course (if in fee structure)."""
    roll_no = input("Enter Roll Number: ").strip()
    if roll_no not in students_db:
        print("Student not found!")
        return
    course_name = input("Enter Course Name: ").strip()
    if course_name in fee_structure:
        amount = fee_structure[course_name]
        students_db[roll_no]['Fees Paid'] += amount
        total_paid = students_db[roll_no]['Fees Paid']
        print(f"Fees of {amount} paid successfully for {students_db[roll_no]['Name']}.")
        print(f"Total Fees Paid: {total_paid}")
    else:
        print("Course not found in fee structure.")

def view_fees_history():
    """Display the total fees a student has paid so far."""
    roll_no = input("Enter Roll Number: ").strip()
    if roll_no not in students_db:
        print("Student not found!")
        return
    total_paid = students_db[roll_no]['Fees Paid']
    print(f"Total Fees Paid by {students_db[roll_no]['Name']}: {total_paid}")

# ----------------------------- REPORTING & ANALYSIS -----------------------------
def export_attendance_report():
    """Export a student's attendance to a CSV file."""
    roll_no = input("Enter Roll Number: ").strip()
    if roll_no not in attendance_db:
        print("No attendance record found for this student.")
        return

    student_name = students_db.get(roll_no, {}).get('Name', 'Unknown')
    filename = f"attendance_report_{roll_no}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Status"])
        for date, status in attendance_db[roll_no].items():
            writer.writerow([date, status])

    print(f"Attendance report for {student_name} exported to '{filename}'.")

def performance_analysis():
    """Calculate and display a student's average marks across all graded courses."""
    roll_no = input("Enter Roll Number: ").strip()
    if roll_no not in students_db:
        print("Student not found!")
        return

    student_name = students_db[roll_no]['Name']
    grades_dict = students_db[roll_no]['Grades']
    marks_dict = students_db[roll_no]['Marks']

    total_courses = len(grades_dict)
    if total_courses == 0:
        print("No grades found for this student.")
        return

    total_marks = 0
    for mark in marks_dict.values():
        try:
            total_marks += float(mark)
        except ValueError:
            # In case a non-numeric value was assigned accidentally
            continue

    average_marks = total_marks / total_courses
    print(f"\nPerformance Analysis for {student_name}:")
    print(f"Average Marks: {average_marks:.2f}")

# ----------------------------- MAIN MENU -----------------------------
def main_menu():
    while True:
        print("Education Trust Nasra School - School Management System")
        print("1.  Add Student")
        print("2.  Update Student")
        print("3.  Delete Student")
        print("4.  View Students")
        print("5.  Search Student")
        print("6.  Add Course")
        print("7.  Enroll Course")
        print("8.  Remove Course")
        print("9.  Edit Course")
        print("10. View Courses")
        print("11. Mark Attendance")
        print("12. View Attendance")
        print("13. Assign Marks and Grade")
        print("14. View Marks and Grades")
        print("15. Pay Fees")
        print("16. View Fees History")
        print("17. Export Attendance Report")
        print("18. Performance Analysis")
        print("19. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            view_students()
        elif choice == '5':
            search_student()
        elif choice == '6':
            add_course()
        elif choice == '7':
            enroll_course()
        elif choice == '8':
            remove_course()
        elif choice == '9':
            edit_course()
        elif choice == '10':
            view_courses()
        elif choice == '11':
            mark_attendance()
        elif choice == '12':
            view_attendance()
        elif choice == '13':
            assign_marks_and_grade()
        elif choice == '14':
            view_marks_and_grades()
        elif choice == '15':
            pay_fees()
        elif choice == '16':
            view_fees_history()
        elif choice == '17':
            export_attendance_report()
        elif choice == '18':
            performance_analysis()
        elif choice == '19':
            print("Exiting | Education Trust Nasra School - School Management System")
            break
        else:
            print("Invalid choice. Please try again.")
        
# ----------------------------- RUN THE PROGRAM -----------------------------
if __name__ == "__main__":
    main_menu()