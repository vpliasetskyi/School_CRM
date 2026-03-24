

#Student: stores student_id, name, grade_level
class Student:
    def __init__(self, student_id, name, grade_level):
        self.student_id = student_id
        self.name = name
        self.grade_level = grade_level
 
    def display_info(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Grade: {self.grade_level}")
 
    def __str__(self):
        return f"Student(ID: {self.student_id}, Name: {self.name}, Grade: {self.grade_level})"
 
 
#Class: stores class_id, class_name, teacher, and a list of enrolled students
class Class:
    def __init__(self, class_id, class_name, teacher):
        self.class_id = class_id
        self.class_name = class_name
        self.teacher = teacher
        self.enrolled_students = []
 
    def add_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            print(f"✅ {student.name} added to {self.class_name}")
        else:
            print(f"⚠️ {student.name} is already enrolled in {self.class_name}")
 
    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            print(f"✅ {student.name} removed from {self.class_name}")
        else:
            print(f"⚠️ {student.name} is not enrolled in {self.class_name}")
 
    def list_students(self):
        print(f"\n📚 Students in {self.class_name} (Teacher: {self.teacher}):")
        if not self.enrolled_students:
            print("   No students enrolled yet.")
        else:
            for student in self.enrolled_students:
                print(f"   • {student.name} (ID: {student.student_id})")
 
    def __str__(self):
        return f"Class(ID: {self.class_id}, Name: {self.class_name}, Teacher: {self.teacher}, Students: {len(self.enrolled_students)})"
 
 
#Grade: links a Student and Class with a score; converts score to letter grade
class Grade:
    def __init__(self, grade_id, student, class_obj, score):
        self.grade_id = grade_id
        self.student = student
        self.class_obj = class_obj
        self.score = score
 
    def get_letter_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"
 
    def display_grade(self):
        letter = self.get_letter_grade()
        print(f"Grade ID: {self.grade_id} | Student: {self.student.name} | "
              f"Class: {self.class_obj.class_name} | Score: {self.score} | Letter: {letter}")
 
    def __str__(self):
        letter = self.get_letter_grade()
        return f"Grade(ID: {self.grade_id}, Student: {self.student.name}, Class: {self.class_obj.class_name}, Score: {self.score}, Letter: {letter})"
 
 
#School: central manager holds all students, classes, and grades
class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []
        self.classes = []
        self.grades = []
 
    #add_student,find_student,list_all_students
    def add_student(self, student_id, name, grade_level):
        for student in self.students:
            if student.student_id == student_id:
                print(f"❌ Student with ID {student_id} already exists!")
                return None
        new_student = Student(student_id, name, grade_level)
        self.students.append(new_student)
        print(f"✅ Student {name} added successfully!")
        return new_student
 
    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        print(f"❌ Student with ID {student_id} not found!")
        return None
 
    def list_all_students(self):
        print(f"\n🎓 Students at {self.school_name}:")
        print("-" * 50)
        if not self.students:
            print("No students enrolled yet.")
        else:
            for student in self.students:
                student.display_info()
        print("-" * 50)
 
    # add_class , find_class , list_all_classes
    def add_class(self, class_id, class_name, teacher):
        for class_obj in self.classes:
            if class_obj.class_id == class_id:
                print(f"❌ Class with ID {class_id} already exists!")
                return None
        new_class = Class(class_id, class_name, teacher)
        self.classes.append(new_class)
        print(f"✅ Class {class_name} added successfully!")
        return new_class
 
    def find_class(self, class_id):
        for class_obj in self.classes:
            if class_obj.class_id == class_id:
                return class_obj
        print(f"❌ Class with ID {class_id} not found!")
        return None
 
    def list_all_classes(self):
        print(f"\n📚 Classes at {self.school_name}:")
        print("-" * 50)
        if not self.classes:
            print("No classes available yet.")
        else:
            for class_obj in self.classes:
                print(f"ID: {class_obj.class_id} | {class_obj.class_name} | Teacher: {class_obj.teacher} | Students: {len(class_obj.enrolled_students)}")
        print("-" * 50)
 
    # enroll_student_in_class funcion
    def enroll_student_in_class(self, student_id, class_id):
        student = self.find_student(student_id)
        if not student:
            return False
        class_obj = self.find_class(class_id)
        if not class_obj:
            return False
        class_obj.add_student(student)
        return True
 
    # add_grade , list_grades_for_student , list_grades_for_class , calculate_student_average functions
    def add_grade(self, grade_id, student_id, class_id, score):
        student = self.find_student(student_id)
        if not student:
            return None
        class_obj = self.find_class(class_id)
        if not class_obj:
            return None
        if student not in class_obj.enrolled_students:
            print(f"❌ {student.name} is not enrolled in {class_obj.class_name}!")
            return None
        for grade in self.grades:
            if grade.grade_id == grade_id:
                print(f"❌ Grade with ID {grade_id} already exists!")
                return None
        new_grade = Grade(grade_id, student, class_obj, score)
        self.grades.append(new_grade)
        print(f"✅ Grade added for {student.name} in {class_obj.class_name}: {score}")
        return new_grade
 
    def list_grades_for_student(self, student_id):
        student = self.find_student(student_id)
        if not student:
            return
        print(f"\n📊 Grades for {student.name}:")
        print("-" * 50)
        student_grades = [g for g in self.grades if g.student.student_id == student_id]
        if not student_grades:
            print("No grades recorded yet.")
        else:
            for grade in student_grades:
                grade.display_grade()
        print("-" * 50)
 
    def list_grades_for_class(self, class_id):
        class_obj = self.find_class(class_id)
        if not class_obj:
            return
        print(f"\n📊 Grades for {class_obj.class_name}:")
        print("-" * 50)
        class_grades = [g for g in self.grades if g.class_obj.class_id == class_id]
        if not class_grades:
            print("No grades recorded yet.")
        else:
            for grade in class_grades:
                grade.display_grade()
        print("-" * 50)
 
    def calculate_student_average(self, student_id):
        student = self.find_student(student_id)
        if not student:
            return None
        student_grades = [g for g in self.grades if g.student.student_id == student_id]
        if not student_grades:
            print(f"{student.name} has no grades yet.")
            return None
        average = sum(grade.score for grade in student_grades) / len(student_grades)
        print(f"📈 {student.name}'s average grade: {average:.2f}")
        return average
 
 
#main: seeds sample data, then runs the interactive menu
def main():
    school = School("Python High School")
 
    print("=" * 60)
    print("🏫 WELCOME TO THE SCHOOL MANAGEMENT SYSTEM 🏫")
    print("=" * 60)
 
    print("\n📝 Adding sample students...")
    school.add_student(1001, "Alice Johnson", 10)
    school.add_student(1002, "Bob Smith", 11)
    school.add_student(1003, "Charlie Brown", 9)
    school.add_student(1004, "Diana Prince", 12)
    school.add_student(1005, "Evan Wright", 10)
 
    print("\n📝 Adding sample classes...")
    school.add_class(201, "Mathematics", "Dr. Smith")
    school.add_class(202, "Science", "Ms. Davis")
    school.add_class(203, "English Literature", "Mr. Johnson")
    school.add_class(204, "History", "Mrs. Williams")
 
    print("\n📝 Enrolling students in classes...")
    school.enroll_student_in_class(1001, 201)
    school.enroll_student_in_class(1001, 202)
    school.enroll_student_in_class(1002, 201)
    school.enroll_student_in_class(1002, 203)
    school.enroll_student_in_class(1003, 201)
    school.enroll_student_in_class(1003, 204)
    school.enroll_student_in_class(1004, 202)
    school.enroll_student_in_class(1004, 203)
    school.enroll_student_in_class(1005, 201)
    school.enroll_student_in_class(1005, 204)
 
    print("\n📝 Adding sample grades...")
    school.add_grade(301, 1001, 201, 95)
    school.add_grade(302, 1001, 202, 88)
    school.add_grade(303, 1002, 201, 78)
    school.add_grade(304, 1002, 203, 92)
    school.add_grade(305, 1003, 201, 85)
    school.add_grade(306, 1003, 204, 90)
    school.add_grade(307, 1004, 202, 96)
    school.add_grade(308, 1004, 203, 89)
    school.add_grade(309, 1005, 201, 82)
    school.add_grade(310, 1005, 204, 75)
 
    print("\n" + "=" * 60)
    print("✅ SETUP COMPLETE! Here's the current status:")
    print("=" * 60)
 
    school.list_all_students()
    school.list_all_classes()
 
    print("\n📊 Example: Alice's Grades")
    school.list_grades_for_student(1001)
 
    print("\n📊 Example: Math Class Grades")
    school.list_grades_for_class(201)
 
    print("\n📊 Example: Student Averages")
    school.calculate_student_average(1001)
    school.calculate_student_average(1002)
 
    while True:
        print("\n" + "=" * 60)
        print("🏫 MAIN MENU")
        print("=" * 60)
        print("1. List all students")
        print("2. List all classes")
        print("3. Add a new student")
        print("4. Add a new class")
        print("5. Enroll student in class")
        print("6. Add a grade")
        print("7. View student grades")
        print("8. View class grades")
        print("9. Calculate student average")
        print("0. Exit")
        print("-" * 60)
 
        choice = input("Enter your choice (0-9): ")
 
        match choice:
            case "1":
                school.list_all_students()
            case "2":
                school.list_all_classes()
            case "3":
                print("\n➕ Add New Student")
                try:
                    student_id = int(input("Enter student ID: "))
                    name = input("Enter student name: ")
                    grade_level = int(input("Enter grade level (9-12): "))
                    school.add_student(student_id, name, grade_level)
                except ValueError:
                    print("❌ Invalid input! Please enter numbers for ID and grade level.")
            case "4":
                print("\n➕ Add New Class")
                try:
                    class_id = int(input("Enter class ID: "))
                    class_name = input("Enter class name: ")
                    teacher = input("Enter teacher name: ")
                    school.add_class(class_id, class_name, teacher)
                except ValueError:
                    print("❌ Invalid input! Please enter a number for class ID.")
            case "5":
                print("\n📝 Enroll Student")
                try:
                    student_id = int(input("Enter student ID: "))
                    class_id = int(input("Enter class ID: "))
                    school.enroll_student_in_class(student_id, class_id)
                except ValueError:
                    print("❌ Invalid input! Please enter numbers for IDs.")
            case "6":
                print("\n📝 Add Grade")
                try:
                    grade_id = int(input("Enter grade ID: "))
                    student_id = int(input("Enter student ID: "))
                    class_id = int(input("Enter class ID: "))
                    score = float(input("Enter score (0-100): "))
                    if 0 <= score <= 100:
                        school.add_grade(grade_id, student_id, class_id, score)
                    else:
                        print("❌ Score must be between 0 and 100!")
                except ValueError:
                    print("❌ Invalid input! Please check your entries.")
            case "7":
                print("\n📊 View Student Grades")
                try:
                    student_id = int(input("Enter student ID: "))
                    school.list_grades_for_student(student_id)
                except ValueError:
                    print("❌ Invalid input! Please enter a number.")
            case "8":
                print("\n📊 View Class Grades")
                try:
                    class_id = int(input("Enter class ID: "))
                    school.list_grades_for_class(class_id)
                except ValueError:
                    print("❌ Invalid input! Please enter a number.")
            case "9":
                print("\n📈 Calculate Student Average")
                try:
                    student_id = int(input("Enter student ID: "))
                    school.calculate_student_average(student_id)
                except ValueError:
                    print("❌ Invalid input! Please enter a number.")
            case "0":
                print("\n👋 Thank you for using the School Management System. Goodbye!")
                break
            case _:
                print("❌ Invalid choice. Please try again.")
 
        input("\nPress Enter to continue...")
 
 
if __name__ == "__main__":
    main()

