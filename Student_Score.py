class Building:
    def __init__(self, name):
        self.name = name
        self.classrooms = []  # Array to hold classroom objects

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)
        self.classrooms.sort(key=lambda c: c.name)  # Sort classrooms by name

    def display_building_info(self):
        print(f"Building: {self.name}")

        count = 1
        for classroom in self.classrooms:
            classroom.display_students(count)
            count += 1

    class Classroom:
        def __init__(self, name):
            self.name = name
            self.students = []  # Array to hold student objects

        def add_student(self, name, score):
            student = self.Student(
                name, score
            )  # FIX: use the nested class, not self.students
            self.students.append(student)

        def display_students(self, count):
            print(
                f"\nClassroom {count}: {self.name}"
            )  # ADD: show which classroom this is
            print("\nAll Students: ")

            counter = 1
            for student in self.students:
                student.introduction(counter)
                counter += 1

        class Student:  # FIX: moved out of display_students,
            def __init__(self, name, score):  # now a proper nested class of Classroom
                self.name = name
                self.score = score
                if self.score < 0 or self.score > 100:
                    raise ValueError("Score must be between 0 and 100.")

            def introduction(self, number):
                print(f"\n Student {number}")
                print(f"Student Name  : {self.name}")
                print(f"Student Score : {self.score}\n")


building_list = []  # FIX: renamed from "Classroom" — that name was shadowing the class

while True:
    building_name = input("\nEnter Building Name (or type 'stop' to finish): ")
    if building_name.lower() == "stop":
        break

    building = Building(building_name)

    while True:
        classroom_numbers = input(
            "\nEnter Classroom Numbers (or type 'stop' to finish): "
        )
        if classroom_numbers.lower() == "stop":
            break

        classroom = Building.Classroom(
            int(classroom_numbers)
        )  # FIX: reference nested class properly

        while True:
            name = input("\nEnter Student Name (or type 'stop' to finish): ")
            if name.lower() == "stop":
                break

            score = float(input("Enter Student Score: "))

            classroom.add_student(name, score)

        building.add_classroom(
            classroom
        )  # FIX: actually attach the classroom to the building

    building_list.append(
        building
    )  # FIX: collect buildings so we can loop over them later

for index, building in enumerate(building_list, start=1):
    print(f"\n===== Building {index} =====")
    building.display_building_info()