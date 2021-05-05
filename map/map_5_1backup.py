import pyglet
from pyglet.gl import *
from pyglet.window import mouse
import math

window = pyglet.window.Window(1080, 720)
batch = pyglet.graphics.Batch()
dic_blocs = {1: pyglet.resource.image("image/herbe1.png"), 2: pyglet.resource.image("image/herbe2.png"),
             3: pyglet.resource.image("image/herbe3.png"), 4: pyglet.resource.image("image/terre1.png"),
             5: pyglet.resource.image("image/terre2.png"), 6: pyglet.resource.image("image/terre3.png"),
             7: pyglet.resource.image("image/terre4.png"), 8: pyglet.resource.image("image/fondtest.png"),
             9: pyglet.resource.image("image/arbre.png")}

# theme = pyglet.resource.media('son/ylia.mp3')
# theme.play()

fichier_carte = open("carte.csv", "r", encoding="utf-8", errors='ignore')
carte = [[int(c) for c in ligne.rstrip().split(";")] for ligne in fichier_carte]
fichier_carte.close()

fichier_decors = open("carte_decors.csv", "r", encoding="utf-8", errors='ignore')
carte_decors = [[int(d) for d in ligne.rstrip().split(";")] for ligne in fichier_decors]
fichier_decors.close()


def create_map():
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


@window.event
def on_mouse_release(x, y, button, modifiers):
    mouse_ = [x, y, button]
    if mouse_[2] == mouse.LEFT:
        coords = get_coords_grid(mouse_)
        print(search_path((coords[0] - 11, coords[1] + 11)))


def get_coords_grid(mouse_):
    # penser à partir de la case de référence (celle du perso)
    alpha = -math.atan(1 / 2)
    beta = math.atan(1 / 2)
    y2 = (mouse_[0] * math.sin(beta) - mouse_[1] * math.cos(beta)) / (
                math.cos(alpha) * math.sin(beta) - math.sin(alpha) * math.cos(beta))
    print("-----")
    print(y2)
    x2 = (mouse_[1] * math.cos(alpha) - mouse_[0] * math.sin(alpha)) / (
                math.cos(alpha) * math.sin(beta) - math.sin(alpha) * math.cos(beta))
    print(x2)
    coords = ((x2 // 35.77709), (y2 // 35.77709))  # -(window.height//2)//32+1)
    print(coords)
    return coords


def search_path(coords):
    print(coords)
    visited = {(0, 0): 0}  # changer par les coordonnés du perso
    traiter = [(0, 0)]
    while len(traiter) != 0:
        current = traiter[0]
        del traiter[0]
        print("visited:", visited)
        print("traiter", traiter)
        bords = get_walkable(current)  # les alentour du point
        for bord in bords:
            print("bord: ", bord)
            if not (bord in visited.keys()):  # si la bordure n'est pas déjà traitée
                traiter.append(bord)
                visited[bord] = visited[current] + 1
                if bord == (int(coords[0]), int(coords[1])):
                    break
    print(visited[coords])
    return visited


def valid(point):
    if point[0] >= 0 and point[1] >= 0:
        if carte[point[0]][point[1]] != 0:
            if carte_decors[point[0]][point[1]] == 0:
                return True
    return False


def get_walkable(point):
    borders = []
    if valid((point[0] + 1, point[1])):
        borders.append((point[0] + 1, point[1]))
    if valid((point[0] - 1, point[1])):
        borders.append((point[0] - 1, point[1]))
    if valid((point[0], point[1] + 1)):
        borders.append((point[0], point[1] + 1))
    if valid((point[0], point[1] - 1)):
        borders.append((point[0], point[1] - 1))
    return borders


def get_path(visited):
    print(visited)


def create_decors():
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


@window.event
def on_draw():
    window.clear()
    dic_blocs[8].blit(0, 0)
    create_map()
    create_decors()


def run():
    pyglet.app.run()


run()
