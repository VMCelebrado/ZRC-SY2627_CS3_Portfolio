class Student:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

#FOR TESTING PURPOSES ONLY:
# student1 = Student("Alice")
# student2 = Student("Bob")
#
# course = Course("Computer Science")
#
# course.add_student(student1)
# course.add_student(student2)
#
# print(course.name)
#
# for student in course.students:
#     print(student.name)