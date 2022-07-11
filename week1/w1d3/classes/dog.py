from classes.animal import Animal

class Dog( Animal ):
    def __init__(self, name, owner, breed, color):
        super().__init__( name, owner, breed)
        self.color = color

    # overriding
    def print_info(self):
        super().print_info()
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")
        
    def walk_animal(self):
        print("i am a dog so i need to be walked two times a day")

