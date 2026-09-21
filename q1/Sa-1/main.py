class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = False
        self.__grade = None
        self.__submitted_files = []

    def __validate_grade(self, score):
        if score < 0 or score > 100:
            print("[Error] Grade must be between 0 and 100.")
            return False
        return True

    def __check_submission(self):
        if len(self.__submitted_files) == 0:
            return False
        return True

    def __is_duplicate(self, filename):
        if filename in self.__submitted_files:
            return True
        return False

    def add_file(self, filename):
        if self.__is_duplicate(filename):
            print(f"[Warning] '{filename}' is already attached!")
            return

        self.__submitted_files.append(filename)
        self.__is_submitted = True

        print(f"[Success] {self.student_name} attached "f"'{filename}'. Total files: {len(self.__submitted_files)}")

    def remove_file(self, filename):
        if self.__grade is not None:
            print(
                f"[Warning] {self.student_name} cannot remove files. "
                f"Assignment already graded.")
            return

        if filename in self.__submitted_files:
            self.__submitted_files.remove(filename)
            if len(self.__submitted_files) == 0:
                self.__is_submitted = False

            print(f"[Success] {self.student_name} removed "f"'{filename}'.")
        else:
            print(f"[Error] '{filename}' was not found.")

    def assign_grade(self, score):
        if not self.__check_submission():
            print(f"[Error] Cannot grade. No files submitted "f"for {self.student_name}.")
            return

        if self.__validate_grade(score):
            self.__grade = score
            print(f"[Success] Grade {score} officially assigned "f"to {self.student_name}.")

    def view_files(self):
        return self.__submitted_files

    def get_status_report(self):
        if self.__is_submitted:
            status = f"Submitted ({len(self.__submitted_files)} files)"
        else:
            status = "Missing"

        if self.__grade is None:
            grade = "Not Graded"
        else:
            grade = self.__grade

        return (f"ID: {self.student_id} | Name: {self.student_name} "f"| Status: {status} | Grade: {grade}")


print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
print()

student1 = AssignmentSubmission("Alex Gonzaga", "pshs-1090-x", "CS-101", "2026-10-01")
student2 = AssignmentSubmission("Adelle", "pshs-1920-x", "CS-103", "2026-10-01")
student3 = AssignmentSubmission("Juan dela Cruz", "pshs-1033-x", "CS-101", "2026-10-01")
student4 = AssignmentSubmission("Maria Santos", "pshs-1044-x", "CS-101", "2026-10-01")
student5 = AssignmentSubmission("Jose Reyes", "pshs-1055-x", "CS-101", "2026-10-01")

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}")
print()

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}")
print()

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py")
print(f"Juan's Files: {student3.view_files()}")
print()

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
