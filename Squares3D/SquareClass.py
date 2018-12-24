from OpenGL.GL import *

COLORS = ((1,1,0),(1,0,0),(0,1,0),(0.5,0,1))

class SquareClass():


    def __init__(self, row, col, color_index, offset):

        self.x = (-2*offset + col*offset)
        self.y = (2*offset - row*offset)
        self.z = 0

        self.color_factor = 0.3
        self.color_index = color_index
        self.color = (COLORS[self.color_index][0] * self.color_factor,
                      COLORS[self.color_index][1] * self.color_factor,
                      COLORS[self.color_index][2] * self.color_factor)

        self.vertices = (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
        )

        self.faces = (
            (0, 1, 2, 3),
            (3, 2, 7, 6),
            (4, 5, 1, 0),
            (6, 7, 5, 4),
            (1, 5, 7, 2),
            (4, 0 , 3, 6)
        )

    def colorUpdate(self):
        self.color = (COLORS[self.color_index][0] * self.color_factor,
                      COLORS[self.color_index][1] * self.color_factor,
                      COLORS[self.color_index][2] * self.color_factor)

    def activate(self):
        self.color_factor = 1
        self.color = COLORS[self.color_index]

    def deactivate(self):
        self.color_factor = 0.3
        self.colorUpdate()

    def flipColor(self):
        self.color_index = (self.color_index + 1) % 4
        self.colorUpdate()

    def getColorIndex(self):
        return self.color_index

    def setColorIndex(self, value):
        self.color_index = value
        self.colorUpdate()

    def draw(self):

        glPushMatrix()
        glTranslate(self.x,self.y, self.z)
        glBegin(GL_TRIANGLES)
        for face in self.faces:
            glColor3fv(self.color)
            glVertex3fv(self.vertices[face[0]])
            glVertex3fv(self.vertices[face[1]])
            glVertex3fv(self.vertices[face[3]])
            glVertex3fv(self.vertices[face[2]])
            glVertex3fv(self.vertices[face[3]])
            glVertex3fv(self.vertices[face[1]])
        glEnd()
        glPopMatrix()