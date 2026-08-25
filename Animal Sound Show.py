from abc import ABC , abstractmethod


class animal (ABC):
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display (self):
            print(f"Name: {self.name}")
            print(f"Habitat: {self.habitat}")

    @abstractmethod
    def speak(self):
                pass

class dog(animal):

    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed

    def speak(self):
        print(f"{self.name} is a {self.breed} and barks: Woof!")


class parrot(animal):

        def __init__(self, name, habitat, phrase):
                    super().__init__(name, habitat)
                    self.phrase = phrase

        def speak(self):
                     print(f"{self.name} says: {self.phrase}")

class lion(animal):

    def __init__(self, name, habitat, pride):
        super().__init__(name, habitat)
        self.pride = pride

    def speak(self):
        print(f"{self.name} is part of the {self.pride} pride and roars: ROAR!")


dog = dog("Buddy", "Domestic", "Golden Retriever")
parrot = parrot("Polly", "Tropical Rainforest", "Hello!")
lion = lion("Simba", "Savannah", "Pride")  

print("-----Animal Sound Show-----")
for animal in [dog, parrot, lion]:
    animal.display()
    animal.speak()
    print("----------------------------")