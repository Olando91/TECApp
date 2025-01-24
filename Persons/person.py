from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, first_name: str, last_name: str, courses=None):
        if courses is None:
            courses = list()
        self.first_name = first_name
        self.last_name = last_name
        self.courses = courses
    
    def add_course(self, course_id: int):
        self.courses.append(course_id)

    def remove_course(self, course_id: int):
        del self.courses[course_id]
    
    def show_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"