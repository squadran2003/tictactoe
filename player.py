class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.character = ''
        self.squares = []

    def set_character(self, char):
        self.character = char
