from functools import reduce

my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = [5, 10, 15]

def multiply_by_two(num):
    return num * 2

def check_if_odd(num):
    return num % 2 != 0

def accumulator(acc, item):
    return acc + item

print(list(map(multiply_by_two, [1, 2, 3, 4, 5])))
print(list(filter(check_if_odd, [1, 2, 3, 4, 5])))
print(list(zip(my_list, your_list, their_list)))
print(reduce( accumulator, my_list, 0))

# done with lambdas
print(list(map(lambda item: item * 5, my_list)))
print(reduce(lambda acc, item: acc + item, your_list, 0))
print(list(filter(lambda item: item %2 != 0, their_list)))