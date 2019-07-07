class Board:
    squares = 9
    occupied = False

    def __init__(self):
        self.matrix = [["_","_","_"],["_","_","_"],["_","_","_"]]
        self.positions_occupied = {}

    def assign(self, position, player):
        self.occupied = False
        row, col = position
        row = row -1
        col = col -1
        if (row,col) in self.positions_occupied.values():
            self.occupied = True
        else:
            self.positions_occupied.update({player.name:(row,col)})
            self.matrix[row][col] = player.character
            self.squares-=1

    def show(self):
        result = ""
        for row in self.matrix:
            result+= ",".join(row)+"\n"
        return result


if __name__=='__main__':
    board = Board()
    n = int(input("no of players? "))
    players = []
    for i in range(0, n):
        players.append(create_player(i+1))
    while board.squares > 0:
        for i in range(len(players)):
            player = players[i]
            print("Player {} make a move".format(player.name))
            print(board.show())
            row = int(input("enter a row number?  "))
            col = int(input("enter a col number?  "))
            board.assign((row, col), player)
            while board.occupied:
                print("sorry that position was taken")
                row = int(input("enter a row number?  "))
                col = int(input("enter a col number?  "))
                board.assign((row,col), player)
