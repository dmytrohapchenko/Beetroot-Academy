class Animal:
    def talk(self):
        raise TypeError("Abstract animal can't talk")


class Dog(Animal):
    def talk(self):
        print('woof woof')


class Cat(Animal):
    def talk(self):
        print('meow')


thomas = Cat()
billy = Dog()

print(thomas.talk())
print(billy.talk())

def func(animal):
    animal.talk()


func(billy)
func(thomas)
