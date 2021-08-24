#Error Handling

while True:
    try:
        age = int(input('What is your age? '))
        10 / age
    except ValueError as err:
        print(f'please enter a number. {err}')
    except ZeroDivisionError as err:
        print(f'please enter an age higher than 0. {err}')
    else:
        print('thank you')
        break