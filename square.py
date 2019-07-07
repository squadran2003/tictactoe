class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = "{}{}".format(self.x, self.y)
        # default character in the square
        self.character = '_'
        self.filled = False

    # adding a getter method to access the id property
    def get_id(self):
        return self.id

    def set_character(self, character):
        self.character = character
        # when a square gets a new character set it to filled
        self.filled = True
