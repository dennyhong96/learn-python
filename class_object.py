from Student import Student, GraduateStudent

student1 = Student("Denny", "IS", 3.4, False)
print(student1.name)

student2 = Student("Pam", "IS", 3, True)
print(student2.name)

print(student2.greeting())

print(student2.gpa)
student2.moregpa(0.3)
print(student2.gpa)

student3 = GraduateStudent("Denny", 3.6, False)
print(student3.level)
print(student3.greeting())
# print(student3.major)

print(student1.on_honor_roll())
print(student2.on_honor_roll())
print(student3.on_honor_roll())
