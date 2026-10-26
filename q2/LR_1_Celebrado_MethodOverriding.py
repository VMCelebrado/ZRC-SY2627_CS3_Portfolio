class Animal:
    def __init__(self, name):
        self.__name = name  

    def get_name(self):
        return self.__name

    def eat(self):
        print(f"{self.__name} eats food!")

    def make_sound(self):
        print(f"{self.__name} makes a sound!")


class Lion(Animal):
    def eat(self):
        print(f"{self.get_name()} eats fresh meat!")

    def make_sound(self):
        print(f"{self.get_name()} roars loudly!")


class Elephant(Animal):
    def eat(self):
        print(f"{self.get_name()} eats grass and fruits!")

    def make_sound(self):
        print(f"{self.get_name()} trumpets!")


class Monkey(Animal):
    def eat(self):
        print(f"{self.get_name()} eats bananas!")

    def make_sound(self):
        print(f"{self.get_name()} chatters!")

generic_animal = Animal("Generic Animal")
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

animals = [generic_animal, lion, elephant, monkey]

for animal in animals:
    animal.make_sound()
    animal.eat()
    print()
