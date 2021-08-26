def generator_function(num):
    for i in range(num):        
        yield i * 2

# for item in generator_function(1000000):
#     print(item)

g = generator_function(100)

print(next(g))
print(next(g))
print(next(g))
