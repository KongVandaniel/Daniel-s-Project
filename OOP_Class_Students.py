# Class List
class A05:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduction(self):
        print("My Name Is", self.name)
        print("Im", self.age, "Years Old")

students = [] # Array

while True:
        name = input("Enter Your Name: ")
        if name == "stop":
            break

        age = int(input("Enter Your Age: "))

        student = A05(name, age)
        students.append(student)

print("\nAll Students: ")

for student in students:
        student.introduction()