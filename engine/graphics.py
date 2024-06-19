import pygame


class draw:
    def __init__(self, screen):
        self.screen = screen

    def draw_circle(self, color, x, y, radius):
        position = pygame.Vector2(x, y)
        pygame.draw.circle(self.screen, color, position, radius)

    def draw_rect(self, color, x1, y1, x2, y2, width):
        rect_rect = pygame.Rect(x1, y1, x2, y2)
        pygame.draw.rect(self.screen, color, rect_rect, width)
