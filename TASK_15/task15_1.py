class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(
            f"Hello, my name is {self.firstname} {self.lastname}"
            f" and I'm {self.age} years old"
        )


result = Person("Carl", "Jonson", 26)
result.talk()
