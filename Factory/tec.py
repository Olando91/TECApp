import os
import platform
from Persons.teacher import Teacher

class Tec:
    def __init__(self):
        self.course_list = ["IoT_Embedded", "Python", "BigData_1", "Softwaresikkerhed_og_test", "Serversideprogrammering"]
        self.teachers = list()

    def add_teacher(self):
        self._clear_terminal()

        first_name = input("Angiv lærens fornavn: ")
        last_name = input("Angiv lærens efternavn: ")
        self._get_list_of_courses()
        print("Angiv fag: ")
        choice = input("Vælg et fag fra listen: ")

        teacher = Teacher(first_name, last_name)
        teacher.add_course(self.course_list[int(choice) -1])
        self.teachers.append(teacher)

        print(f"\n{first_name} {last_name} er nu oprettet som lærer med følgende fag:")
        for i in teacher.courses:
            print(f"- {i}")



    def update_teacher(self):
        return
    
    def show_all_teachers(self):
        return
    
    def save_and_exit(self):
        with open("teachers.txt", "w", encoding="utf-8") as file:
            for teacher in self.teachers:
                courses_str = ",".join(teacher.courses)
                file.write(f"{teacher.first_name}, {teacher.last_name},{courses_str}\n")
        print("Data gemt")
        exit()

    
    def _get_list_of_courses(self):
        counter = 1
        for course in self.course_list:
            print(f"[{counter}] {course}")
            counter += 1

    def _clear_terminal(self):
        system_name = platform.system().lower()
        if system_name == "windows":
            os.system("cls")
        else:
            os.system("clear")