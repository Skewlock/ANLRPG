import pyglet
from pyglet.gl import *

class Ennemy:
    
    def __init__(self, hp, mp, pm=1):
        self.x = 9
        self.y = 9
        self.hp = hp
        self.mana = mp
        self.pm = pm
    
    def move(self):
        # déplacement du sprite et des ennemis
        pass
    
    
    def draw(self, window):
        self.sprite = pyglet.sprite.Sprite(self.image, x = 15, y = window.height/2 )
        xpos = (self.x * 32 + self.y * 32) + 15
        ypos = (window.height/2 + self.x * 16 + self.y * -16) - 4
        self.sprite.update(x = xpos, y = ypos)  # update le sprite du perso et ça position
        self.sprite.draw()
    

class John(Ennemy):
    
    def __init__(self, hp, mp, pm, ar):
        Ennemy.__init__(self, hp, mp, pm)
        self.armure = ar
        self.image = pyglet.image.load("character/sprites/bonome.png")
        
    
    def use_spell(self):
        pass