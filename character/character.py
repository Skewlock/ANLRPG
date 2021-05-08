import pyglet
from pyglet.gl import *


class Character:

    def __init__(self, x, y):
        self.x = x  # position sur la carte
        self.y = y
        self.sprite = pyglet.sprite.Sprite(pyglet.resource.image("character/sprites/bonome.png"))  #sprite

    def move_character(self, path):
        print("-----------------------------\n", path)
        anim_transition = 0.1  # faire une transition pour pas avoir de tp case par case
        for case in path:
            print(self.x, self.y)
            if case[0] > self.x:
                for i in range(10):
                    self.x += anim_transition
            elif case[0] < self.x:
                for i in range(10):
                    self.x -= anim_transition
            elif case[1] > self.y:
                for i in range(10):
                    self.y += anim_transition
            elif case[1] > self.y:
                for i in range(10):
                    self.y -= anim_transition
            self.x = round(self.x)
            self.y = round(self.y)
        print("oui ", self.x, self.y)

    def draw(self, window):
        self.sprite.update(x=window.width/2, y=window.height/2)  # update le sprite du perso et ça position
        self.sprite.draw()  # dessiner le sprite
