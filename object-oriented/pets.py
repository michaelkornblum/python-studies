class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return (f'{self.name} is just walking around.')


class Simon(Cat):
    def sing(self, sounds):
        return(f'{sounds}')

class Sally(Cat):
    def sing(self, sounds):
        return(f'{sounds}')

# 1
class Roosevelt(Cat):
    def sing(self, sounds):
        return(f'{sounds}')

# 2
simon = Simon('Simon', 3)
sally = Sally('Sally', 3)
roosevelt = Roosevelt('Roosevelt', 15)

# 3
my_cats = [simon, sally, roosevelt]

# 4
pets = Pets(my_cats)
pets.walk()


