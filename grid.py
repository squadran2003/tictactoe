from square import Square


class Grid:
    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.squares = []

    def set_rows(self, rows):
        self.rows = rows

    def set_columns(self, columns):
        self.columns = columns

    def create_grid(self):
        """create squares on the grid"""
        for i in range(self.columns):
            for j in range(self.rows):
                # create a new square object passing in x(row), y(column)
                square = Square(i, j)
                # add the square
                self.squares.append([square])

    def show_grid(self):
        grid_str = ""
        count = 0
        for i in range(len(self.squares)):
            # print out each squares character
            grid_str+="[{}]".format(self.squares[i][0].character)
            if i==2  or i==5 or i==8:
                grid_str+="\n"
        print(grid_str)

    def get_square(self, x, y):
        """
        params: x: outer list index, y inner list index
        return: returns a square object

        """

        return self.squares[x][y]

    def open_squares(self):
        """
        number of empty squares

        return: integer of open squares, or squares that dont have a charc
        """
        return len([square for square in self.squares if not square[0].filled])
