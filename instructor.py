from nss_person import NSSPerson

class Instructor(NSSPerson):
    def __init__(self, first_name, last_name, slack_handle, specialty):
        super().__init__(first_name, last_name, slack_handle)
        self.specialty = specialty

    def assign_exercise(self, Student, Exercise):
        Student.current_exercises.append(Exercise)