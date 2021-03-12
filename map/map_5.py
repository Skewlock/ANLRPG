import pyglet
from pyglet.gl import *

window = pyglet.window.Window(1720, 1080)
batch = pyglet.graphics.Batch()
dic_blocs = {1: pyglet.resource.image("map/image/herbe1.png"), 2: pyglet.resource.image("map/image/herbe2.png"),
             3: pyglet.resource.image("map/image/herbe3.png"), 4: pyglet.resource.image("map/image/terre1.png"),
             5: pyglet.resource.image("map/image/terre2.png"), 6: pyglet.resource.image("map/image/terre3.png"),
             7: pyglet.resource.image("map/image/terre4.png"), 8: pyglet.resource.image("map/image/fondtest.jpg")}

f = open("map/carte.csv", "r", encoding="utf-8", errors='ignore')
carte = [[int(c) for c in ligne.rstrip().split(";")] for ligne in f]
f.close()


def create_map():
    L = []  # liste stockant les sprites de blocs
    l = 0  # variable pour la pos des blocs utilisé pour les colonnes
    t = 0
    for i in range(len(carte)):
        l = l + 16
        k = 0
        t = t + 0.01
        z = pyglet.graphics.OrderedGroup(0 - t)
        for j in range(len(carte[i])):
            if carte[i][j] != 0:
                L.append(pyglet.sprite.Sprite(dic_blocs[carte[i][j]], x=-1500 - 16 + k + l, y=360 - k / 2 + l / 2 - 1,
                                              batch=batch, group=z))
            k = k + 16

    batch.draw()


@window.event
def on_draw():
    window.clear()

    # sprite = pyglet.sprite.Sprite(dic_blocs[carte[0][0]], x= 240, y = 240, batch = batch)
    # batch.draw()
    create_map()


def run():
    pyglet.app.run()
