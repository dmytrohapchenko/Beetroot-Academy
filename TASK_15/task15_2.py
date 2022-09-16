class Dog:
    age_factor = 7

    def __init__(self, age):
        self.equivalent_age = None
        self.age = age

    def human_age(self):
        self.equivalent_age = self.age * self.age_factor
        return f'{self.age} years dog age is equivalent to ' \
               f'{self.equivalent_age} years of human age.'


snoop_dog = Dog(14)
print(snoop_dog.human_age())
