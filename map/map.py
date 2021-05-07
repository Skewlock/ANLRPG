import pyglet
from pyglet.gl import *

batch = pyglet.graphics.Batch()
dic_blocs = {1: pyglet.resource.image("map/image/herbe1.png"), 2: pyglet.resource.image("map/image/herbe2.png"),
             3: pyglet.resource.image("map/image/herbe3.png"), 4: pyglet.resource.image("map/image/terre1.png"),
             5: pyglet.resource.image("map/image/terre2.png"), 6: pyglet.resource.image("map/image/terre3.png"),
             7: pyglet.resource.image("map/image/terre4.png"), 8: pyglet.resource.image("map/image/fondtest.png"),
             9: pyglet.resource.image("map/image/arbre.png")} # on défini les blocs de base

# theme = pyglet.resource.media('son/ylia.mp3')
# theme.play()

fichier_carte = open("map/carte.csv", "r", encoding="utf-8", errors='ignore') # on crée la carte basée sur le csv
carte = [[int(c) for c in ligne.rstrip().split(";")] for ligne in fichier_carte]
fichier_carte.close()

fichier_decors = open("map/carte_decors.csv", "r", encoding="utf-8", errors='ignore') # on crée la carte des décors
carte_decors = [[int(d) for d in ligne.rstrip().split(";")] for ligne in fichier_decors]
fichier_decors.close()


def create_map(window):
    L = []  # liste stockant les sprites de blocs
    l = 0  # variable pour la pos des blocs utilisé pour les colonnes
    t = 0
    for i in range(len(carte)):
        l = l + 32
        k = 0
        t = t + 0.01
        z = pyglet.graphics.OrderedGroup(0 - t)
        for j in range(len(carte[i])):
            if carte[i][j] != 0:
                L.append(pyglet.sprite.Sprite(dic_blocs[carte[i][j]], x=-32 + k + l,
                                              y=window.height / 2 - 64 - k / 2 + l / 2 - 1,
                                              batch=batch, group=z))
                L[-1].update(scale=2)
            k = k + 32

    batch.draw()


def create_decors(window):
    L_decors = []
    l = 0
    t = 0
    for i in range(len(carte_decors)):
        l = l + 32
        k = 0
        t = t + 0.01
        z = pyglet.graphics.OrderedGroup(0 - t)
        for j in range(len(carte_decors[i])):
            if carte_decors[i][j] != 0:
                L_decors.append(pyglet.sprite.Sprite(dic_blocs[carte_decors[i][j]], x=-32 + k + l,
                                                     y=window.height / 2 - 64 - k / 2 + l / 2 - 1,
                                                     batch=batch, group=z))
                L_decors[-1].update(scale=2)
            k = k + 32

    batch.draw()


def load_map(window):
    dic_blocs[8].blit(0, 0)
    create_map(window)
    create_decors(window)