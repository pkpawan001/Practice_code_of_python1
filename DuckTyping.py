class Dog:
    def walk(self):
        print("Dog is walking")
    def eat(self):
        print("Dog is eating")

class Duck:
    def walk(self):
        print("Duck is walking")
    def eat(self):
        print("Duck is eating")
#Duck typing example person doesn't know about pet functionality 
def person(pet):
    pet.walk()  
    pet.eat()


dog =Dog()
person(dog)

