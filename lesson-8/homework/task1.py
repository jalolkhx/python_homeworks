class Animal:
    def __init__(self, name, typeAnimal, sound):
        self.name = name
        self.typeAnimal = typeAnimal
        self.sound = sound

    def sleep(self):
        return f"{self.name} ({self.typeAnimal}) is sleeping"
    
    def eat(self, food):
        return f"{self.name} ({self.typeAnimal}) is eating {food}"
    
    def sound(self):
        return f"{self.name} ({self.typeAnimal}) is making sound of {self.sound}"
    
    def run(self):
        return f"{self.name} ({self.typeAnimal}) can run"
    
class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, typeAnimal='Chicken', sound='ququ')

    def produce_egg(self):
        return f"{self.name} (Chicken) can produce eggs"
    
class Fish(Animal):
    def __init__(self, name):
        super().__init__(name, typeAnimal='Fish', sound='blublu')

    def run(self):
        return f"{self.name} (Fish) cannot run"
    
    def swim(self):
        return f"{self.name} (Fish) can swim"

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, typeAnimal='Cow', sound='Moo')

    def produce_milk(self):
        return f"{self.name} (Cow) is producing milk"
    
sarah = Chicken('Sarah')
print(sarah.eat('corn'))
print(sarah.produce_egg())

sazancik = Fish('Sazancik')
print(sazancik.run())
print(sazancik.swim())
