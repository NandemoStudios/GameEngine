import pygame
import engine.graphics as graphics
import engine.actors as actors
import keyboard
import engine.input as Input

class Engine():
    def __init__(self):
        self.screen = pygame.display.set_mode((900, 600))
        self.Clock = pygame.time.Clock()
        self.running = True
        self.backgroundColor = 'White'
        self.draw = graphics.draw(self.screen)
        self.actors = actors
        self.Input = Input
        self.Actors = []

    def flip(self):
        self.screen.fill(self.backgroundColor)

    def tick(self):
        pygame.display.flip()
        self.Clock.tick(60)

    def newActor(self, color, **kwargs):
        if "shape" in kwargs:
            shape = kwargs.get("shape")
        else:
            shape = "circle"
        new_Actor = actors.Actor(self, color, shape)
        self.Actors.append(new_Actor)
        return new_Actor

    def renderActors(self):
        if len(self.Actors) > 0:
            for ac in self.Actors:
                ac.renderActor()
