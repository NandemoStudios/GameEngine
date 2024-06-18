import pygame
import engine.graphics as graphics
import engine.actors as actors


class Engine():
    def __init__(self):
        self.screen = pygame.display.set_mode((900, 600))
        self.Clock = pygame.time.Clock()
        self.running = True
        self.backgroundColor = 'White'
        self.draw = graphics.draw(self.screen)
        self.actors = actors
        self.Actors = []

    def flip(self):
        self.screen.fill(self.backgroundColor)

    def tick(self):
        pygame.display.flip()
        self.Clock.tick(60)

    def newActor(self, startx, starty, color, radius):
        new_Actor = actors.Actor(self, startx, starty, radius, color)
        self.Actors.append(new_Actor)

    def renderActors(self):
        if len(self.Actors) > 0:
            for ac in self.Actors:
                ac.renderActor()
