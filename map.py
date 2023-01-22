class Map:
    def __init__(self, spaces):
        self.board = [['e' for i in range(spaces)]
                      for j in range(spaces)]

    def placeElement(self, pos, type):
        self.board[pos[0]][pos[1]] = type

    def size(self):
        return len(self.board)

    def get(self, pos):
        return self.board[int(pos[0])][int(pos[1])]

    def checkSpace(self, pos):
        if pos[0] < 0 or pos[0] >= len(self.board):
            return (False, None)
        if pos[1] < 0 or pos[1] >= len(self.board):
            return (False, None)

        return (True, self.get(pos))
