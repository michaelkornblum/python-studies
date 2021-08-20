class User():
    def sign_in(self):
        print('logged in')

    def attack(User):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        # Override class method with parent
        User.attack(self)
        print(f'Casting a {self.power} spell.')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'Firing a crossbow. Arrows remaining: {self.arrows}')


wizard1 = Wizard('Bob', 'Fireball')
archer1 = Archer('Steve', 100)
# print(wizard1.sign_in())
# print(archer1.sign_in())
# wizard1.attack()
# archer1.attack()
# print(isinstance(wizard1, Wizard))
# print(isinstance(archer1, User))
# print(isinstance(wizard1, object))

def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)