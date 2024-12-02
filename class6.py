class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.attendance = False

    def mark_attendance(self):
        self.attendance = True



class AttendanceBook:
    def __init__(self):
        self.students = []
        self.student_ids = set()

    def add_student(self, name, student_id):
        if student_id not in self.student_ids:
            student = Student(name, student_id)
            self.students.append(student)
            self.student_ids.add(student_id)

    def mark_student_attendance(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                student.mark_attendance()
                break

    def get_attendance_summary(self):
        return {
            "출석": sum(student.attendance for student in self.students),
            "결석": sum(not student.attendance for student in self.students),
        }

    def get_student_list(self):
        return [student.name for student in self.students if student.attendance]






