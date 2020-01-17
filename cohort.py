class Cohort:
    def __init__(self, name):
        self.cohort_name = name
        self.cohort_students = list()
        self.cohort_instructors = list()

    def add_student(self, Student):
        self.cohort_students.append(Student)
        Student.cohort = self.cohort_name

    def add_instructor(self, Instructor):
        self.cohort_instructors.append(Instructor)
        Instructor.cohort = self.cohort_name