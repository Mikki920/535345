
#class Animal:

    #sound = "Undefined"
    #habitat = "Undefined"

   # def __init__(self, name, species, color, can_fly=False, can_swim=False):

        #self.name = name
        #self.species = species
        #self.color = color
        #self.can_fly = can_fly
        #self.can_swim = can_swim

    #def make_sound(self):
        #print(f"{self.name} says: {self.sound}")

    #def move(self):
        #if self.can_fly and self.can_swim:
            #print(f"{self.name} can fly and swim.")
        #elif self.can_fly:
            #print(f"{self.name} can fly.")
        #elif self.can_swim:
            #print(f"{self.name} can swim.")
        #else:
            #print(f"{self.name} can neither fly nor swim.")


#class Zoo:
    #def __init__(self, animals):
        #self.animals = animals

    #def perform_activities(self):
        #for animal in self.animals:
            #print(f"\nActivities for {animal.name}:")
            #animal.make_sound()
            #animal.move()



#tiger = Animal("Tiger", "Mammal", "Orange and black", False, False)
#eagle = Animal("Eagle", "Bird", "Brown", True, False)
#fish = Animal("Fish", "Fish", "Silver", False, True)
#frog = Animal("Frog", "Amphibian", "Green", False, True)


#zoo = Zoo([tiger, eagle, fish, frog])


#zoo.perform_activities()

ЗАВДАННЯ 2

class Car:

    fuel_type = "Petrol"
    wheels = 4

    def __init__(self, make, model, year, color, speed=0):

        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed

    def start_engine(self):
        print(f"The {self.color} {self.year} {self.make} {self.model}'s engine is now running.")

    def accelerate(self, mph):
        self.speed += mph
        print(f"The {self.color} {self.year} {self.make} {self.model} is now moving at {self.speed} mph.")

    def brake(self):
        if self.speed > 0:
            print(f"The {self.color} {self.year} {self.make} {self.model} is now slowing down.")
            self.speed = 0
        else:
            print(f"The {self.color} {self.year} {self.make} {self.model} is already stationary.")

    def turn_off_engine(self):
        print(f"The {self.color} {self.year} {self.make} {self.model}'s engine is now turned off.")



car1 = Car("Toyota", "Camry", 2022, "Blue")
car2 = Car("Ford", "Mustang", 2023, "Red", speed=20)


car1.start_engine()
car1.accelerate(30)
car1.brake()
car1.turn_off_engine()

car2.start_engine()
car2.accelerate(10)
car2.brake()
car2.turn_off_engine()

