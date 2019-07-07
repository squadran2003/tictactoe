from grid import Grid
from player import Player


class Game:
    def __init__(self):
        self.over = False
        # create the grid
        self.grid = Grid()
        self.grid.create_grid()
        self.player = object

    def pick_position(self):
        x,y = tuple(
            input("Your position ? [example 00 for 1st square] ")
        )
        square = self.grid.get_square(int(x), int(y))
        if square.filled:
            print("the square is taken!!")
            self.pick_position()
        square.set_character(self.player.character)
        self.player.squares.append(square)
        self.grid.show_grid()


    def help_text(self):
        print("""
            Welcome to Tic tac toe built by
            ** andreas cormack.
            here is how you pick a square,
            first square is 0,0, seconds 1,0 and so on,
            see below example
            [
             00    10    20
             []    []    []
             30    40    50
             []    []    []
             60    70    80
             []    []    []
            ]

        """)

    def start_game(self):
        # print out a help text
        self.help_text()
        # get inputs to create the player object
        player_name = input("What is your name? ")
        while not player_name:
            player_name = input("What is your name? ")
        age = input("What is your age? ")
        while not age:
            age = input("What is your age? ")
        character = input("What is your character X or O ? ")
        while not character:
            character = input("What is your character X or O ? ")
        # create a player object
        self.player = Player(player_name, age)
        # set the players character
        self.player.set_character(character)
        # show the initial grid
        self.grid.show_grid()
        print("""
            Please choose a position, supply the position
            of the square as shown above. First
            square is 0,0
        """)
        # keep looping over till all squares are filled
        while self.grid.open_squares()>0:
            self.pick_position()
