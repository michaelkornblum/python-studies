def hello():
    print('hello')

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*****')
        func(*args, **kwargs)
        print('*****')
    return wrap_func

@my_decorator
def hello(greet, name):
    print(f'{greet}, {name}!')

hello('Hello', 'Michael')
