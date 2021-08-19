#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Michael', 50)
cat2 = Cat('Sheila', 52)
cat3 = Cat('Roosevelt', 15)

# 2 Create a function that finds the oldest cat
def find_oldest(*args):
    cats = []
    for cat in args:
        cats.append(cat.__dict__)
    cat_ages = []
    for cat in cats:
        cat_ages.append(cat['age'])
    return max(cat_ages)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {find_oldest(cat1, cat2, cat3)} years old')