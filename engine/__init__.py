import pygame
import engine.graphics as graphics


class Engine():
    def __init__(self):
        self.screen = pygame.display.set_mode((900, 600))
        self.Clock = pygame.time.Clock()
        self.running = True
        self.backgroundColor = 'White'
        self.draw = graphics.draw(self.screen)

    def flip(self):
        self.screen.fill(self.backgroundColor)

    def tick(self):
        pygame.display.flip()
        self.Clock.tick(60)