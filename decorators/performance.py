from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f'execution time: {end - start} ms')
        return result
    return wrapper

@performance
def greeting(greeting, name):
    return f'{greeting}, {name}!'

greeting('hello', 'michael')
