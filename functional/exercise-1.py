from functools import reduce
my_pets = ['sisi', 'bibi', 'titi', 'carla']
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
scores = [73, 20, 65, 19, 76, 100, 88]

def cap_me(item):
    return item.capitalize()

def over_fifty(item):
    return item > 50

def accumulator(acc, item):
    return acc + item

def merge_lists(*args):
    reduce(accumulator, args, [])

print(list(map(cap_me, my_pets)))

print(list(zip(sorted(my_numbers), my_strings)))

print(list(filter(over_fifty, scores)))

print(reduce(accumulator, my_numbers + scores, 0))

