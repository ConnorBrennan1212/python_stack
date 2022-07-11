from classes.animal import Animal

class Cat( Animal ):
    def __init__(self, name, owner, breed, age):
        super().__init__(name, owner, breed)
        self.age = age

    def walk_animal(self):
        print( "I dont need to be walked ")

    def print_info(self):
        super().print_info()
        print(f"Breed: {self.breed}")
        print(f"age: {self.age}")