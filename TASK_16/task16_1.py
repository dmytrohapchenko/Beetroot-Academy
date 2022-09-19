class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"Student's name is {self.name}"


class Teacher(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def __str__(self):
        return f"Teacher's name is {self.name}, salary: {self.salary}"


print(Student('Robert Polson'))
print(Teacher('Lida Romanova', 14_000))
