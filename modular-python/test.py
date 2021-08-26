from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7, 7]

print(Counter(li))

my_dict = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(my_dict['c'])