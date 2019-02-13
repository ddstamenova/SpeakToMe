"""

class Maze contains information about the maze;

The maze is represented by a list of 0 and 1 values
where 0 represents no block/obstacle and 1 represents block/obstacle;

"""


class Maze:

    def __init__(self):
        self.x_axis_size = 13
        self.y_axis_size = 10
        self.layout = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                       1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
                       1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
                       1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
                       1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                       1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1,
                       1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                       1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                       1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
                       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def draw(self, display_surf, image_surf):
        x = 0  # pixel of window (width)
        y = 0  # pixel of window (height)

        for i in range(0, self.x_axis_size * self.y_axis_size):
            if self.layout[x + (y * self.x_axis_size)] == 1:
                display_surf.blit(image_surf, (x * 60, y * 60))  # multiplied by 60 - size of block/player

            # move to next column of blocks
            x = x + 1

            # move to next row of blocks, if end of current row is reached
            if x > self.x_axis_size - 1:
                x = 0
                y = y + 1
