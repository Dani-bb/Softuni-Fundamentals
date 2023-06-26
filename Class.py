class Class:
    _students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class._students_count > 0:
            self.students.append(name)
            self.grades.append(grade)
            Class._students_count -= 1

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        average_grade = self.get_average_grade()
        student_list = ", ".join(self.students)
        return f"The students in {self.name}: {student_list}. Average grade: {average_grade}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
