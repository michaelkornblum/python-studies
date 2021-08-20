class PlayerCharacter():
    membership = True
    def __init__(self, name="anon", age=0):
        self.name = name
        self.age = age

    def run(self):
        return f"{self.name} is running."

    def shout(self):
        return f"My name is {self.name}, and I am {self.age} years old!!!"

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

player_one = PlayerCharacter('Michael', 50)
print(player_one.shout())
# player_two = PlayerCharacter('Roosevelt', 15)
# print(player_one.name, player_one.age)
# print(player_two.name, player_two.age)
# print(player_two.run())

# print(PlayerCharacter.adding_things(2, 3))

# player3 = PlayerCharacter.adding_things(2, 3)
# print(player3.age)



