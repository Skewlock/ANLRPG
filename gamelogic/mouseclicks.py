from pyglet.window import mouse
import math


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

    

def move_character(character, mouse_):
    coords = get_coords_grid(mouse_)
    visited, coords = search_path(
        (coords[0] - 11, coords[1] + 11), character)  # les -11 étaient pour un test, enlever pour la version finale
    path = get_path(visited, coords)
    character.move_character(path)


def search_path(coords, character):
    print(coords)
    visited = {(character.x, character.y): 0}  # changer par les coordonnés du perso
    traiter = [(character.x, character.y)]
    current = (character.x, character.y)
    while len(traiter) != 0 and current != coords:
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
    print(visited[coords])
    return visited, coords


def valid(point):
    fichier_carte = open("map/carte.csv", "r", encoding="utf-8", errors='ignore')  # on crée la carte basée sur le csv
    carte = [[int(c) for c in ligne.rstrip().split(";")] for ligne in fichier_carte]
    fichier_carte.close()

    fichier_decors = open("map/carte_decors.csv", "r", encoding="utf-8", errors='ignore')  # on crée la carte des décors
    carte_decors = [[int(d) for d in ligne.rstrip().split(";")] for ligne in fichier_decors]
    fichier_decors.close()

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


def get_path(visited, coords):
    print("----------------------\n", visited, coords)
    path = [coords]
    goal = visited[coords]
    dist = visited[coords]
    while len(path) != goal and dist > 0:
        dist -= 1
        print(path, dist)
        for i in visited.items():
            if i[1] == dist:
                if is_neighbour(i[0], path[-1]):
                    path.append(i[0])
    path.reverse()
    return path


def is_neighbour(test, base):
    if (test[0] + 1, test[1]) == base or (test[0] - 1, test[1]) == base or (test[0], test[1] + 1) == base or (
            test[0], test[1] - 1) == base:
        return True
