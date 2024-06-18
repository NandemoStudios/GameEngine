import pygame

class draw:
    def __init__(self, screen):
        self.screen = screen

    def draw_circle(self, color, x, y, radius):
        position = pygame.Vector2(x, y)
        pygame.draw.circle(self.screen, color, position, radius)