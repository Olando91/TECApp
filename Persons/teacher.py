from Persons.person import Person

class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, courses=None):
        if courses is None:
            courses = list()
        super().__init__(first_name, last_name)
        self.courses = courses

    def add_course(self, course: str):
        self.courses.append(course)