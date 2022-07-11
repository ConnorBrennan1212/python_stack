class Animal:
    def __init__(self, name, owner, breed):
        self.name = name
        self.owner = owner
        self.breed = breed

    def print_info( self):
        print(f"Name of animal: {self.name}")
        print(f"Owner: {self.owner}")
# polymorphism
    def walk_animal(self):
        raise NotImplementedError 