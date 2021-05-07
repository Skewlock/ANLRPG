import pyglet
from pyglet.gl import *

class Character:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pyglet.sprite.Sprite(pyglet.resource.image("character/sprites/bonome.png"))
        
    def move_character(self, path):
        for case in path:
            for i in range(0, 1, 0.1):
                if case[0] > self.x:
                    self.x += i
                if case[0] < self.x:
                    self.x -= i
                if case[1] > self.x:
                    self.y += i
                if case[1] > self.x:
                    self.y -= i