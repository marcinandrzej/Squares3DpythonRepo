import random

from OpenGL.GL import *

from SquareClass import SquareClass

class GridClass():

    def __init__(self, offset):

        self.offset = offset

        self.player_pointer = [0, 0]

        self.y_rotation = 0
        self.x_rotation = 0

        self.grid = []
        for rows in range(5):
            self.grid.append([])
            for cols in range(5):
                rand_index = random.randrange(4)
                self.grid[rows].append(SquareClass(rows, cols, rand_index, self.offset))

        self.grid[0][0].activate()

    def flipColor(self):
            row =  self.player_pointer[0]
            col =  self.player_pointer[1]
            self.grid[row][col].setColorIndex((self.grid[row][col].getColorIndex() + 1) % 4)
            self.updateNeighbours(row, col)

    def updateNeighbours(self, row, col):
        if row > 0 and row < 4 and col > 0 and col < 4:
            self.grid[row - 1][col].setColorIndex((self.grid[row - 1][col].getColorIndex() + 1) % 4)
            self.grid[row + 1][col].setColorIndex( (self.grid[row + 1][col].getColorIndex() + 1) % 4)
            self.grid[row][col - 1].setColorIndex( (self.grid[row][col - 1].getColorIndex() + 1) % 4)
            self.grid[row - 1][col - 1].setColorIndex( (self.grid[row - 1][col - 1].getColorIndex() + 1) % 4)
            self.grid[row + 1][col - 1].setColorIndex( (self.grid[row + 1][col - 1].getColorIndex() + 1) % 4)
            self.grid[row][col + 1].setColorIndex( (self.grid[row][col + 1].getColorIndex() + 1) % 4)
            self.grid[row - 1][col + 1].setColorIndex( (self.grid[row - 1][col + 1].getColorIndex() + 1) % 4)
            self.grid[row + 1][col + 1].setColorIndex( (self.grid[row + 1][col + 1].getColorIndex() + 1) % 4)
        elif row == 0 and col == 0:
            self.grid[row][col + 1].setColorIndex((self.grid[row][col + 1].getColorIndex() + 1) % 4)
            self.grid[row + 1][col].setColorIndex((self.grid[row + 1][col].getColorIndex() + 1) % 4)
            self.grid[row + 1][col + 1].setColorIndex((self.grid[row + 1][col + 1].getColorIndex() + 1) % 4)
        elif row == 0 and col == 4:
            self.grid[row][col - 1].setColorIndex((self.grid[row][col - 1].getColorIndex() + 1) % 4)
            self.grid[row + 1][col].setColorIndex((self.grid[row + 1][col].getColorIndex() + 1) % 4)
            self.grid[row + 1][col - 1].setColorIndex((self.grid[row + 1][col - 1].getColorIndex() + 1) % 4)
        elif row == 4 and col == 0:
            self.grid[row][col + 1].setColorIndex((self.grid[row][col + 1].getColorIndex() + 1) % 4)
            self.grid[row - 1][col].setColorIndex((self.grid[row - 1][col].getColorIndex() + 1) % 4)
            self.grid[row - 1][col + 1].setColorIndex((self.grid[row - 1][col + 1].getColorIndex() + 1) % 4)
        elif row == 4 and col == 4:
            self.grid[row][col - 1].setColorIndex((self.grid[row][col - 1].getColorIndex() + 1) % 4)
            self.grid[row - 1][col].setColorIndex((self.grid[row - 1][col].getColorIndex() + 1) % 4)
            self.grid[row - 1][col - 1].setColorIndex((self.grid[row - 1][col - 1].getColorIndex() + 1) % 4)
        elif row == 0 and col > 0 and col < 4:
            self.grid[row + 1][col].setColorIndex( (self.grid[row + 1][col].getColorIndex() + 1) % 4)
            self.grid[row][col - 1].setColorIndex( (self.grid[row][col - 1].getColorIndex() + 1) % 4)
            self.grid[row + 1][col - 1].setColorIndex( (self.grid[row + 1][col - 1].getColorIndex() + 1) % 4)
            self.grid[row][col + 1].setColorIndex( (self.grid[row][col + 1].getColorIndex() + 1) % 4)
            self.grid[row + 1][col + 1].setColorIndex( (self.grid[row + 1][col + 1].getColorIndex() + 1) % 4)
        elif row == 4 and col > 0 and col < 4:
            self.grid[row - 1][col].setColorIndex((self.grid[row - 1][col].getColorIndex() + 1) % 4)
            self.grid[row][col - 1].setColorIndex( (self.grid[row][col - 1].getColorIndex() + 1) % 4)
            self.grid[row - 1][col - 1].setColorIndex( (self.grid[row - 1][col - 1].getColorIndex() + 1) % 4)
            self.grid[row][col + 1].setColorIndex( (self.grid[row][col + 1].getColorIndex() + 1) % 4)
            self.grid[row - 1][col + 1].setColorIndex( (self.grid[row - 1][col + 1].getColorIndex() + 1) % 4)
        elif col == 0 and row > 0 and row < 4:
            self.grid[row - 1][col].setColorIndex((self.grid[row - 1][col].getColorIndex() + 1) % 4)
            self.grid[row + 1][col].setColorIndex( (self.grid[row + 1][col].getColorIndex() + 1) % 4)
            self.grid[row][col + 1].setColorIndex( (self.grid[row][col + 1].getColorIndex() + 1) % 4)
            self.grid[row - 1][col + 1].setColorIndex( (self.grid[row - 1][col + 1].getColorIndex() + 1) % 4)
            self.grid[row + 1][col + 1].setColorIndex( (self.grid[row + 1][col + 1].getColorIndex() + 1) % 4)
        elif col == 4 and row > 0 and row < 4:
            self.grid[row - 1][col].setColorIndex((self.grid[row - 1][col].getColorIndex() + 1) % 4)
            self.grid[row + 1][col].setColorIndex( (self.grid[row + 1][col].getColorIndex() + 1) % 4)
            self.grid[row][col - 1].setColorIndex( (self.grid[row][col - 1].getColorIndex() + 1) % 4)
            self.grid[row - 1][col - 1].setColorIndex( (self.grid[row - 1][col - 1].getColorIndex() + 1) % 4)
            self.grid[row + 1][col - 1].setColorIndex( (self.grid[row + 1][col - 1].getColorIndex() + 1) % 4)

    def checkWin(self):
        if (self.grid[0][0].getColorIndex() == self.grid[0][1].getColorIndex() == self.grid[0][2].getColorIndex() ==
                self.grid[0][3].getColorIndex() == self.grid[0][4].getColorIndex() ==
                self.grid[1][0].getColorIndex() == self.grid[1][1].getColorIndex() ==
                self.grid[1][2].getColorIndex() == self.grid[1][3].getColorIndex() == self.grid[1][4].getColorIndex() ==
                self.grid[2][0].getColorIndex() == self.grid[2][1].getColorIndex() ==
                self.grid[2][2].getColorIndex() == self.grid[2][3].getColorIndex() == self.grid[2][4].getColorIndex() ==
                self.grid[3][0].getColorIndex() == self.grid[3][1].getColorIndex() ==
                self.grid[3][2].getColorIndex() == self.grid[3][3].getColorIndex() == self.grid[3][4].getColorIndex() ==
                self.grid[4][0].getColorIndex() == self.grid[4][1].getColorIndex() ==
                self.grid[4][2].getColorIndex() == self.grid[4][3].getColorIndex() == self.grid[4][4].getColorIndex()):
            return True
        else:
            return False

    def moveUp(self):
        if self.player_pointer[0] > 0:
            self.grid[self.player_pointer[0]][self.player_pointer[1]].deactivate()
            self.player_pointer[0] -= 1
            self.grid[self.player_pointer[0]][self.player_pointer[1]].activate()

    def moveDown(self):
        if self.player_pointer[0] < 4:
            self.grid[self.player_pointer[0]][self.player_pointer[1]].deactivate()
            self.player_pointer[0] += 1
            self.grid[self.player_pointer[0]][self.player_pointer[1]].activate()

    def moveRight(self):
        if self.player_pointer[1] < 4:
            self.grid[self.player_pointer[0]][self.player_pointer[1]].deactivate()
            self.player_pointer[1] += 1
            self.grid[self.player_pointer[0]][self.player_pointer[1]].activate()

    def moveLeft(self):
        if self.player_pointer[1] > 0:
            self.grid[self.player_pointer[0]][self.player_pointer[1]].deactivate()
            self.player_pointer[1] -= 1
            self.grid[self.player_pointer[0]][self.player_pointer[1]].activate()

    def draw(self, x_change, y_change):

        if (self.x_rotation + x_change) <= 45 and (self.x_rotation + x_change) >= -45:
            self.x_rotation = self.x_rotation + x_change
        elif (self.x_rotation + x_change) > 45:
            self.x_rotation = 45
        else:
            self.x_rotation = -45

        if (self.y_rotation + y_change) <= 45 and (self.y_rotation + y_change) >= -45:
            self.y_rotation = self.y_rotation + y_change
        elif (self.y_rotation + y_change) > 45:
            self.y_rotation = 45
        else:
            self.y_rotation = -45

        glPushMatrix()
        glRotatef(self.x_rotation, 1, 0, 0)
        glRotatef(self.y_rotation, 0, 1, 0)

        for row in range(5):
            for col in range(5):
                self.grid[row][col].draw()
        glPopMatrix()