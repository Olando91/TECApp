import os
import platform
import json
from Persons.teacher import Teacher
from Persons.student import Student
from Courses.course import Course

# TODO:
# Skal verificere at det kun er bogstaver i input for navn/efternavn
# Man må ikke tilmelde fag man allerede er tilmeldt
# Tilføjer ikke fag korrekt til lærer

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
        self._clear_terminal()

    def add_teacher(self):
        self._clear_terminal()

        first_name, last_name, choice = self._get_input()

        if (first_name == False) or (last_name == False) or (choice == False):
            return

        teacher = Teacher(first_name, last_name)
        teacher.add_course(self.course_list[int(choice) -1].id)
        self.teachers.append(teacher)

        print(f"\n{first_name} {last_name} er nu oprettet som lærer med følgende fag:")
        print(f"- {self.course_list[int(choice) -1].name}")

    def add_student(self):
        self._clear_terminal()

        first_name, last_name, choice = self._get_input()

        if (first_name == False) or (last_name == False) or (choice == False):
            return

        student = Student(first_name, last_name)
        student.add_course(self.course_list[int(choice) -1].id)
        self.students.append(student)

        print(f"\n{first_name} {last_name} er nu oprettet som elev og er tilmeldt følgende fag:")
        print(f"- {self.course_list[int(choice) -1].name}")

    def update_teacher(self):
        self._clear_terminal()
        print("Liste af alle lærer:")
        counter = 1
        for teacher in self.teachers:
            print(f"[{counter}] {teacher.show_full_name()}")
            counter += 1
        while True:
            teacher_choice = input("Vælg en lærer fra listen eller tryk 'e' for at returnere til hovedmenuen: ")
            if teacher_choice == 'e':
                return
            try:
                teacher_choice = int(teacher_choice)
                if 1 <= teacher_choice <= counter -1:
                    break
                else:
                    print("\n\n**Du skal vælge en lære fra listen eller 'e' for at returnere til hovedmenunen**\n\n")
            except ValueError:
                print(f"\n\n**Du skal vælge et tal mellem 1 og {counter -1} eller trykke 'e' for at returnere til hovedmenuen**\n\n")
        
        valgt_lære = self.teachers[int(teacher_choice) - 1]

        print(f"\n\n {valgt_lære.show_full_name()} er tilmeldt følgende fag:")
        for course_id in valgt_lære.courses:
                match = next((match for match in self.course_list if match.id == course_id), None)
                print(f"- {match.name}")
        
        print(f"\n\n[1] Tilføj flere fag for {valgt_lære.show_full_name()}.")
        print("[2] Slet et fag.")
        print("Tryk 'e' for at returnere til hovedmenuen.")
        while True:
            choice = input("Vælg 1 eller 2: ")

            if choice == '1':
                new_course_id = self._get_list_of_courses()
                if new_course_id == 'e':
                    return
                
                valgt_lære.add_course(self.course_list[int(new_course_id) -1].id)
                print(f"\n\n{valgt_lære.show_full_name()} er tilmeldt følgende fag:")
                for course_id in valgt_lære.courses:
                    match = next((match for match in self.course_list if match.id == course_id), None)
                    print(f"- {match.name}")
                print()
                return
            elif choice == '2':
                print(f"\n\nAngiv et fag at slette:")

                course_counter = 1
                for course_id in valgt_lære.courses:
                    match = next((match for match in self.course_list if match.id == course_id), None)
                    print(f"[{course_counter}] {match.name}")
                    course_counter +=1

                while True:
                    course_id_to_delete = input("Vælg et fag fra listen eller tryk 'e' for at returnere til hovedmenuen: ")
                    if course_id_to_delete == 'e':
                        return
                    try:
                        id_to_delete = int(course_id_to_delete)
                        if 1 <= id_to_delete <= course_counter -1:
                            break
                        else:
                            print("\n\n**Du skal vælge et fag fra listen eller trykke 'e' for at returnere til hovedmenuen**\n\n")
                    except ValueError:
                        print(f"\n\n**Input skal være at tal mellem 1 og {course_counter -1} eller 'e' for at returnere til hovedmenuen**\n\n")
                
                valgt_lære.remove_course(int(course_id_to_delete)-1)
                print(f"\n\n{valgt_lære.show_full_name()} er tilmeldt følgende fag:")
                for course_id in valgt_lære.courses:
                    match = next((match for match in self.course_list if match.id == course_id), None)
                    print(f"- {match.name}")
                print()
                return
            elif choice == 'e':
                return
            else:
                print("\n\n**Du skal vælge 1, 2 eller 'e'**\n\n")

        
    def show_all_teachers(self):
        self._clear_terminal()
        print("Liste af alle lærer:")
        for teacher in self.teachers:
            print(f"- {teacher.show_full_name()}, fag:")
            for course_id in teacher.courses:
                match = next((match for match in self.course_list if match.id == course_id), None)
                print(f"     - {match.name}, students:")
                for student in self.students:
                    if course_id in student.courses:
                        print(f"            - {student.show_full_name()}")
    
    def save_and_exit(self):
        data = {
            "teachers": [teacher.__dict__ for teacher in self.teachers],
            "students": [student.__dict__ for student in self.students]
        }
        with open(self.file_name, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("Data gemt")
        exit()

    
    def _get_list_of_courses(self):
        print("Angiv fag: ")
        course_counter = 1
        for course in self.course_list:
            print(f"[{course_counter}] {course.name}")
            course_counter += 1
        while True:
            choice = input("Vælg et fag fra listen eller tryk 'e' for at returnere til hovedmenuen: ")
            if choice.lower() == 'e':
                return 'e'
            try:
                choice_number = int(choice)
                if 1 <= choice_number <= course_counter -1:
                    return choice_number
                else:
                    print(f"\n\n**Ugyldigt valg. Du skal vælge et tal mellem 1 og {course_counter -1} eller tryk 'e' for at returnere til hovedmenuen**\n\n")
            except ValueError:
                print("\n\n**Input skal være et tal eller 'e'.**\n\n")

    def _clear_terminal(self):
        system_name = platform.system().lower()
        if system_name == "windows":
            os.system("cls")
        else:
            os.system("clear")
    
    def _get_input(self):
        print("Tryk 'e' når som helst for at vende tilbage til hovedmenuen.")

        first_name = input("Angiv fornavn: ")
        if first_name.lower() == 'e':
            return False, False, False
        
        last_name = input("Angiv efternavn: ")
        if last_name.lower() == 'e':
            return False, False, False
        
        choice = self._get_list_of_courses()
        if str(choice).lower() == 'e':
            return False, False, False
    
        return first_name, last_name, choice

    def _load_data(self):
        if os.path.exists(f"{self.file_name}"):
            try:
                with open (self.file_name, 'r', encoding="utf-8") as file:
                    data = json.load(file)
                    self.teachers = [Teacher(**teacher) for teacher in data.get("teachers", [])]
                    self.students = [Student(**student) for student in data.get("students", [])]
                        
                print("Data loaded")
            
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Kunne ikke hente data fra {self.file_name}: {e}")
                self.teachers = []
                self.students = []
        else:
            print("Ingen fil fundet, opretter ny liste")
            self.teachers = []
            self.students = []