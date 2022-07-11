# from package_name import module/variable/function/class
from classes.animal import Animal
from classes.dog import Dog
from classes.cat import Cat

max = Animal("max", "alex", "Labrador")

max.print_info()

jagger = Dog( "jagger", "Alfredo", "Golden Retriever", "Yellow")
jagger.print_info()
jagger.walk_animal()

chester = Cat("chester", "Alfredo", "Yellow", 6)
chester.print_info()
chester.walk_animal()