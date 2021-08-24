user1 = {
    'name': 'Sorna',
    'valid': False
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid'] == True:
            fn(*args, **kwargs)
        print('Invalid User')
    return wrapper

@authenticated
def is_authenticated(user):
    print(f'Hello, {user["name"]}')

is_authenticated(user1)
