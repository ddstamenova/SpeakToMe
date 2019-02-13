"""

class Player contains information about the player block;

"""


class Player:

    x_coordinate = 60      # position in width of the window
    y_coordinate = 60      # position in height of the window
    speed = 1              # how many blocks the player moves
    startingPosition = 14  # position in the maze

    """
    functions about the player moving - change coordinates on the window and position in the maze
    """

    def move_right(self):
        self.x_coordinate += 60
        self.startingPosition += 1

    def move_left(self):
        self.x_coordinate -= 60
        self.startingPosition -= 1

    def move_up(self):
        self.y_coordinate -= 60
        self.startingPosition -= 13

    def move_down(self):
        self.y_coordinate += 60
        self.startingPosition += 13
