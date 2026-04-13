class Student:
    def __init__(self, name, surname, age, course):
        self.name = name
        self.surename = surname
        self.age = age
        self.course = course
    def get_full_name(self):
        return f'{self.name} {self.surename}'
