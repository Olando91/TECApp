from Persons.person import Person

class Student(Person):
    def __init__(self, first_name: str, last_name: str, courses=None):
        super().__init__(first_name, last_name, courses)