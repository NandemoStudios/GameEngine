from typing import Any

import engine.graphics
import pygame

acceptedShapes = ['circle', 'rectangle']


class Actor:

    def __init__(self, parent, color, shape):
        self.parent = parent
        self.shape = shape
        self.color = color

        # Setting Defaults
        self.x1 = 0
        self.y1 = 0
        self.height = 1
        self.width = 1
        self.radius = 1

        match self.shape:
            case "circle":
                self.shape = "circle"
            case "rectangle":
                self.shape = "rectangle"
            case _:
                print("That is not a valid shape")

    def setActorSize(self, **kwargs):
        if self.shape == "rectangle":
            self.x1 = kwargs.get("x1")
            self.width = kwargs.get("width")
            self.y1 = kwargs.get("y1")
            self.height = kwargs.get("height")
        if self.shape == "circle":
            self.x1 = kwargs.get('x1')
            self.y1 = kwargs.get('y1')
            self.radius = kwargs.get('radius')

    def renderActor(self):
        if self.shape == 'circle':
            if hasattr(self, 'radius'):
                self.parent.draw.draw_circle(self.color, self.x1, self.y1, self.radius)
        elif self.shape == 'rectangle':
            if hasattr(self, 'height'):
                self.parent.draw.draw_rect(self.color, self.x1, self.y1, self.width, self.height, 1)
