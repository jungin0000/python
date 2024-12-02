class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def calculate_average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0


class GradeBook:
    def __init__(self):
        self.students = []
        self.student_ids = set()

    def add_student(self, name, student_id):
        if student_id not in self.student_ids:
            student = Student(name, student_id)
            self.students.append(student)
            self.student_ids.add(student_id)

    def add_student_score(self, student_id, score):
        for student in self.students:
            if student.student_id == student_id:
                student.add_score(score)
                return
        print("학생을 찾을 수 없습니다.")

    def get_top_students(self, n):
        averages = [(student.name, student.calculate_average()) for student in self.students]
        averages.sort(key=lambda x: x[1], reverse=True)
        return averages[:n]
