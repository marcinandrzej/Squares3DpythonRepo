import pygame
from pygame.locals import *

import random

from OpenGL.GL import *
from OpenGL.GLU import *

from GridClass import GridClass

class MainClass():

    def __init__(self, window_w, window_h, sound):

        pygame.init()
        self.display = (window_w, window_h)
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        pygame.display.set_caption("Squares3D!")
        glEnable(GL_DEPTH_TEST)

        self.x_change = 0
        self.y_change = 0

        self.win = False

        self.sound = pygame.mixer.Sound(sound)

        self.game = GridClass(2.0)

    def eventLoopProcessing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    self.win = False
                    self.game = GridClass(2.0)
                if event.key == pygame.K_w:
                    self.x_change = -2
                if event.key == pygame.K_s:
                    self.x_change = 2
                if event.key == pygame.K_d:
                    self.y_change = -2
                if event.key == pygame.K_a:
                    self.y_change = 2
                if event.key == pygame.K_UP and self.win == False:
                    self.game.moveUp()
                if event.key == pygame.K_DOWN and self.win == False:
                    self.game.moveDown()
                if event.key == pygame.K_RIGHT and self.win == False:
                    self.game.moveRight()
                if event.key == pygame.K_LEFT and self.win == False:
                    self.game.moveLeft()
                if event.key == pygame.K_SPACE and self.win == False:
                    self.game.flipColor()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.x_change = 0
                if event.key == pygame.K_s:
                    self.x_change = 0
                if event.key == pygame.K_d:
                    self.y_change = 0
                if event.key == pygame.K_a:
                    self.y_change = 0

    def checkWinCondition(self):
        if self.win == False:
            self.win = self.game.checkWin()
            if self.win:
                self.sound.play();

    def drawGame(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 50.0)
        glTranslate(0.0, 0.0, -20.0)

        self.game.draw(self.x_change, self.y_change)

        pygame.display.flip()

