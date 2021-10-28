class Animal:
    def __init__(self, legs, type):
        self.legs = legs
        self.type = type
    def describe(self):
        print("This animal is a", self.type, "and has", self.legs, "legs")

class Dog(Animal):
    def __init__(self, legs, type, breed):
        super().__init__(legs,type)
        self.breed = breed

    def Sound(self):
        print("Woof")


Bird = Animal(2,"Aviary")
Bird.describe()

Wambo = Dog(4, "Mammal", "Askal")
Wambo.Sound()
