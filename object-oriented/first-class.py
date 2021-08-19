class PlayerCharacter():
    membership = True
    def __init__(self, name="anon", age=0):
        if age > 18:
            self.name = name
            self.age = age

    def run(self):
        return f"{self.name} is running."

    def shout(self):
        return f"My name is {self.name}!!!"

# player_one = PlayerCharacter('Michael', 50)
player_two = PlayerCharacter('Roosevelt', 15)
# print(player_one.name, player_one.age)
# print(player_two.name, player_two.age)
print(player_two.run())

