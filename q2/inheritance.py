class PSHS_galaxy:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Welcome to Le Galaxy, {self.name}!")

class Nationality(PSHS_galaxy):
    def __init__(self, name, country):
        super().__init__(name)
        self.country = country

    def identity(self):
        print(f"Hello bradar, I am {self.name} from {self.country}")


class Alien(PSHS_galaxy):
    def __init__(self, name, universe):
        super().__init__(name)
        self.universe = universe

    def identity(self):
        print(f"Greetings bradar, I am {self.name} from the {self.universe} universe")

class Filipino(Nationality):
    def __init__(self, name):
        super().__init__(name, "Philippines")

class Indonesian(Nationality):
    def __init__(self, name):
        super().__init__(name, "Indonesia")

class Spaniard(Nationality):
    def __init__(self, name):
        super().__init__(name, "Spain")

class Marvel(Alien):
    def __init__(self, name):
        super().__init__(name, "Marvel")

class Avengers(Alien):
    def __init__(self, name):
        super().__init__(name, "Avengers")

filipino = Filipino("Juan")
indonesian = Indonesian("Budi")
spaniard = Spaniard("Carlos")
marvel = Marvel("Spider-Man")
avengers = Avengers("Iron Man")

for character in [filipino, indonesian, spaniard, marvel, avengers]:
    character.introduce()
    character.identity()
    print() 
