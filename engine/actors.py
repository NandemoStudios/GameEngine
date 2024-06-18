import engine.graphics
import pygame


class Actor:
    def __init__(self, parent, startx, starty, radius, color):
        self.position = pygame.Vector2(startx, starty)
        self.radius = radius
        self.color = color
        self.parent = parent

    def renderActor(self):
        self.parent.draw.draw_circle(self.color, self.position.x, self.position.y, self.radius)
