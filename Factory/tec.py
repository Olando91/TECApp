import os
import platform
import json
from Persons.teacher import Teacher
from Persons.student import Student
from Courses.course import Course

# TODO:
# Må ikke kunne vælge fag der ikke er på listen - ingen bogstaver
# Skal verificere at det kun er bogstaver i input for navn/efternavn

class Tec:
    def __init__(self):
        self.course_list = [
            Course(1 ,"IoT_Embedded"), 
            Course(2, "Python"),
            Course(3, "BigData_1"),
            Course(4, "Softwaresikkerhed_og_test"), 
            Course(5, "Serversideprogrammering")
            ]
        
        self.file_name = "teachers.json"
        self.teachers = list()
        self.students = list()
        self._load_data()

    def add_teacher(self):
        self._clear_terminal()

        first_name, last_name, choice = self._get_input()

        teacher = Teacher(first_name, last_name)
        teacher.add_course(self.course_list[int(choice) -1].id)
        self.teachers.append(teacher)

        print(f"\n{first_name} {last_name} er nu oprettet som lærer med følgende fag:")
        for i in teacher.courses:
            matching_course = next((course for course in self.course_list if course.id == i), "Intet fag fundet")
            print(f"- {matching_course.name}")

    def add_student(self):
        self._clear_terminal()

        first_name, last_name, choice = self._get_input()

        student = Student(first_name, last_name)
        student.add_course(self.course_list[int(choice) -1].id)
        self.students.append(student)

        print(f"\n{first_name} {last_name} er nu oprettet som elev og er tilmeldt følgende fag:")
        for i in student.courses:
            matching_course = next((course for course in self.course_list if course.id == i), "Intet fag fundet")
            print(f"- {matching_course.name}")

    def update_teacher(self):
        return
    
    def show_all_teachers(self):
        return
    
    def save_and_exit(self):
        data = []
        for teacher in self.teachers:
            teacher_data = {
                "first_name": teacher.first_name,
                "last_name": teacher.last_name,
                "courses": [
                    {"course_id": course} for course in teacher.courses
                ],
            }
            data.append(teacher_data)

        with open(f"{self.file_name}", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print("Data gemt")
        exit()

    
    def _get_list_of_courses(self):
        for course in self.course_list:
            print(f"[{course.id}] {course.name}")

    def _clear_terminal(self):
        system_name = platform.system().lower()
        if system_name == "windows":
            os.system("cls")
        else:
            os.system("clear")
    
    def _get_input(self):
        first_name = input("Angiv lærens fornavn: ")
        last_name = input("Angiv lærens efternavn: ")
        self._get_list_of_courses()
        print("Angiv fag: ")
        choice = input("Vælg et fag fra listen: ")
        return first_name, last_name, choice

    def _load_data(self):
        if os.path.exists(f"{self.file_name}"):
            try:
                with open (f"{self.file_name}", "r", encoding="utf-8") as file:
                    data = json.load(file)
                    for teacher_data in data:
                        courses = [
                            course["course_id"] for course in teacher_data["courses"]
                        ] 
                        teacher = Teacher(teacher_data["first_name"], teacher_data["last_name"], courses)
                        self.teachers.append(teacher)
                        
                print("Data loaded")
            
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Kunne ikke hente data fra {self.file_name}: {e}")
                self.teachers = []
        else:
            print("Ingen fil fundet, opretter ny liste")
            self.teachers = []