# student roll no number marks [private] in the form of value key
# calculate grade avg marks is passed or fail add marks

# class room grade section students add students

# REPORT card


class Student:

    def __init__(self, Name, roll_No):
        self.Name = Name
        self.roll_No = roll_No
        self.__marks = {}

    def add_marks(self, subject, marks):
        self.__marks[subject] = marks

    def cal_avg(self):
        total = 0

        for marks in self.__marks.values():
            total += marks

        Average = total / len(self.__marks)
        return Average

    def marks(self):
        return self.__marks

    def is_passed(self):
        is_failed = any(
            [mark < 35 for mark in self.__marks.values()]
        )

        if is_failed:
            print(f"{self.Name} has Failed")
        else:
            print(f"{self.Name} has Passed")

    def grade(self):
        percentage = self.cal_avg()

        if percentage >= 85:
            return "A Grade"
        elif percentage < 85 and percentage > 70:
            return "B Grade"
        else:
            return "C Grade"


class Report_Card:

    @staticmethod
    def genrate_report(student):
        student_mark = student.marks()

        print(f"NAME : {student.Name}")
        print(f"Roll_NO : {student.roll_No}")
        print("-----Marks-----")

        for subject, mark in student_mark.items():
            print(f"{subject} : {mark}")

        print(f"Average of Total Marks : {student.cal_avg()}")
        student.is_passed()
        print(f"Grade : {student.grade()}")


class Classroom:

    def __init__(self, grade, section):
        self.grade = grade
        self.section = section
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def get_list(self):
        for student in self.__students:
            print(f"{student.roll_No} . {student.Name}")

    def class_average(self):
        total = 0

        for student in self.__students:
            total += student.cal_avg()

        Average = total / len(self.__students)
        return Average

    def get_student(self, roll_No):
        for student in self.__students:
            if student.roll_No == roll_No:
                return student

        return None


# Menu

classroom = None

while True:

    print("\n1. Create Classroom")
    print("2. Add Student")
    print("3. Add Marks")
    print("4. Show Students")
    print("5. Generate Report Card")
    print("6. Show Class Average")
    print("7. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":

        grade = input("Enter Grade : ")
        section = input("Enter Section : ")

        classroom = Classroom(grade, section)

        print("Classroom created successfully!")

    elif choice == "2":

        if classroom is None:
            print("Please create a classroom first!")

        else:
            name = input("Enter Student Name : ")
            roll_No = int(input("Enter Roll No : "))

            student = Student(name, roll_No)
            classroom.add_student(student)

            print("Student added successfully!")

    elif choice == "3":

        if classroom is None:
            print("Please create a classroom first!")

        else:
            roll_No = int(input("Enter Roll No : "))
            student = classroom.get_student(roll_No)

            if student is None:
                print("Student not found!")

            else:
                subject = input("Enter Subject : ")
                marks = int(input("Enter Marks : "))

                student.add_marks(subject, marks)

                print("Marks added successfully!")

    elif choice == "4":

        if classroom is None:
            print("Please create a classroom first!")

        else:
            print(f"Grade : {classroom.grade}")
            print(f"Section : {classroom.section}")
            print("-----Students-----")

            classroom.get_list()

    elif choice == "5":

        if classroom is None:
            print("Please create a classroom first!")

        else:
            roll_No = int(input("Enter Roll No : "))
            student = classroom.get_student(roll_No)

            if student is None:
                print("Student not found!")

            elif len(student.marks()) == 0:
                print("No marks added for this student!")

            else:
                Report_Card.genrate_report(student)

    elif choice == "6":

        if classroom is None:
            print("Please create a classroom first!")

        elif len(classroom._Classroom__students) == 0:
            print("No students in classroom!")

        else:
            print(f"Class Average : {classroom.class_average():.2f}")

    elif choice == "7":

        print("Program exited!")
        break

    else:
        print("Invalid choice! Please try again.")