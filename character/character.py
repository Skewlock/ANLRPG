import pyglet
from pyglet.gl import *
import math


class Character:

    def __init__(self, x, y):
        self.x = x  # position sur la carte
        self.y = y
        self.sprite = pyglet.sprite.Sprite(pyglet.resource.image("character/sprites/bonome.png"))  #sprite

    def move_character(self, path):
        print(self.x, self.y)
        anim_transition = 0.01  # on gère l'animation du personnage (le chemin est géré dans mouseclicks)
        for case in path:
            print(self.x, self.y)
            if case[0] > self.x:
                for i in range(10):
                    self.x += anim_transition
            if case[0] < self.x:
                for i in range(10):
                    self.x -= anim_transition
            if case[1] > self.x:
                for i in range(10):
                    self.y += anim_transition
            if case[1] > self.x:
                for i in range(10):
                    self.y -= anim_transition

    def draw(self):
        # self.sprite.update() # update le sprite du perso et ça position
        self.sprite.draw() # dessiner le sprite