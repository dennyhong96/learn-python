class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def greeting(self):
        return f"My name is {self.name} and hello!"

    def moregpa(self, points):
        self.gpa += points

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


class GraduateStudent(Student):
    def __init__(self, name, gpa, is_on_probation):
        self.name = name
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        self.level = "Graduate"

    def greeting(self):
        return f"My name is {self.name} and I am a graduate student"
