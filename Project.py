import os
import pandas as pd

class Student:
    def __init__(self, student_id, name, age, gender, contact_info):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_info = contact_info

class Course:
    def __init__(self, course_id, course_name, description):
        self.course_id = course_id
        self.course_name = course_name
        self.description = description
        self.enrolled_students = []

class Attendance:
    def __init__(self):
        self.attendance_records = {}

    def mark_attendance(self, student_id, course_id, date, status):
        if date not in self.attendance_records:
            self.attendance_records[date] = {}
        self.attendance_records[date][(student_id, course_id)] = status

    def get_attendance_report(self, student_id):
        report = {}
        for date, records in self.attendance_records.items():
            for (s_id, c_id), status in records.items():
                if s_id == student_id:
                    report[date] = status
        return report

class SchoolManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.attendance = Attendance()

    def add_student(self, student_id, name, age, gender, contact_info):
        if student_id in self.students:
            print("\n********* Student ID already exists.**********\n")
        else:
            student = Student(student_id, name, age, gender, contact_info)
            self.students[student_id] = student
            print("\n********* Student added successfully.**********\n")

    def update_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            print("Updating student:")
            name = input("Enter new name (leave blank to keep current): ")
            if name:
                student.name = name
            age = input("Enter new age (leave blank to keep current): ")
            if age:
                student.age = int(age)
            gender = input("Enter new gender (leave blank to keep current): ")
            if gender:
                student.gender = gender
            contact_info = input("Enter new contact info (leave blank to keep current): ")
            if contact_info:
                student.contact_info = contact_info
            print("\n********* Student updated successfully.**********\n")
        else:
            print("\n********* Student not found.**********\n")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("\n********* Student deleted successfully.**********\n")
        else:
            print("\n********* Student not found.**********\n")

    def view_students(self):
        if not self.students:
            print("\n--------- No students available.----------\n")
        else:

            data = {
                "ID": [],
                "Name": [],
                "Age": [],
                "Gender": [],
                "Contact": []
            }
            for student in self.students.values():
                data["ID"].append(student.student_id)
                data["Name"].append(student.name)
                data["Age"].append(student.age)
                data["Gender"].append(student.gender)
                data["Contact"].append(student.contact_info)

            df = pd.DataFrame(data)
            file_name = "student_details.xlsx"
            df.to_excel(file_name, index=False)
            print(f"\n********* Student details saved as '{file_name}'. **********\n")

    def view_courses(self):
        if not self.courses:
            print("\n--------- No courses available.----------\n")
        else:
            print("\n--------- Course Details ----------\n")
            for course in self.courses.values():
                print(f"Course ID: {course.course_id}, Name: {course.course_name}, Description: {course.description}")
            print("\n--------- End of Course Details ----------\n")

    def add_course(self, course_id, course_name, description):
        if course_id in self.courses:
            print("\n********* Course ID already exists.**********\n")
        else:
            course = Course(course_id, course_name, description)
            self.courses[course_id] = course
            print("\n********* Course added successfully.**********\n")

    def enroll_student_in_course(self, student_id, course_id):
        student = self.students.get(student_id)
        course = self.courses.get(course_id)
        if student and course:
            course.enrolled_students.append(student_id)
            print("\n********* Student enrolled in course successfully.**********\n")
        else:
            print("\n********* Student or Course not found.**********\n")

    def mark_attendance(self, student_id, course_id):
        date = input("\t\tEnter the date (YYYY-MM-DD): ")
        status = input("\t\tEnter attendance status (Present/Absent): ")
        self.attendance.mark_attendance(student_id, course_id, date, status)
        print("\n********* Attendance marked successfully.**********\n")

    def generate_attendance_report(self, student_id):
        report = self.attendance.get_attendance_report(student_id)
        if report:
            print(f"\t\tAttendance report for student ID {student_id}:")
            for date, status in report.items():
                print(f"\t\tDate: {date}, Status: {status}")
        else:
            print("\n--------- No attendance records found for this student.----------\n")


def pause_for_main_menu():
    input("\nPress \"ENTER\" to return to the MAIN MENU...")


# Example usage
if __name__ == "__main__":
    sms = SchoolManagementSystem()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("===================================================")
        print("||\t\tSCHOOL MANAGEMENT SYSTEM \t ||")
        print("===================================================")
        print("||                                               ||")
        print("||\t\t1. Add Student                   ||")
        print("||\t\t2. Update Student                ||")
        print("||\t\t3. Delete Student                ||")
        print("||\t\t4. View Students                 ||")
        print("||\t\t5. Add Course                    ||")
        print("||\t\t6. View Courses                  ||")
        print("||\t\t7. Enroll Student in Course      ||")
        print("||\t\t8. Mark Attendance               ||")
        print("||\t\t9. Generate Attendance Report    ||")
        print("||\t\t10. Exit                         ||")
        print("||                                               ||")
        print("===================================================")

        choice = input("Choose an option: ")

        if choice == "1":
            student_id = int(input("\t\tEnter student ID: "))
            name = input("\t\tEnter student name: ")
            age = int(input("\t\tEnter student age: "))
            gender = input("\t\tEnter student gender: ")
            contact_info = input("\t\tEnter contact info: ")
            sms.add_student(student_id, name, age, gender, contact_info)
            pause_for_main_menu()

        elif choice == "2":
            student_id = int(input("\t\tEnter student ID to update: "))
            sms.update_student(student_id)
            pause_for_main_menu()

        elif choice == "3":
            student_id = int(input("\t\tEnter student ID to delete: "))
            sms.delete_student(student_id)
            pause_for_main_menu()

        elif choice == "4":
            sms.view_students()
            pause_for_main_menu()

        elif choice == "5":
            course_id = int(input("\t\tEnter course ID: "))
            course_name = input("\t\tEnter course name: ")
            description = input("\t\tEnter course description: ")
            sms.add_course(course_id, course_name, description)
            pause_for_main_menu()

        elif choice == "6":
            sms.view_courses()
            pause_for_main_menu()

        elif choice == "7":
            student_id = int(input("\t\tEnter student ID to enroll: "))
            course_id = int(input("\t\tEnter course ID: "))
            sms.enroll_student_in_course(student_id, course_id)
            pause_for_main_menu()

        elif choice == "8":
            student_id = int(input("\t\tEnter student ID for attendance: "))
            course_id = int(input("\t\tEnter course ID: "))
            sms.mark_attendance(student_id, course_id)
            pause_for_main_menu()

        elif choice == "9":
            student_id = int(input("\t\tEnter student ID for attendance report: "))
            sms.generate_attendance_report(student_id)
            pause_for_main_menu()

        elif choice == "10":
            print("\t-------- Exiting the system. ---------")
            break

        else:
            print("Invalid choice. Please try again.")
            pause_for_main_menu()
