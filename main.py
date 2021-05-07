"""import networking.client as client


def menu():  # menu dans la console
    print("-------------------------------------")
    print("\t[Menu de connexion]")
    print("[1]: Connexion")
    print("[2]: Register")
    print("[3]: Quitter")
    print("-------------------------------------")
    choice = int(input("Votre choix: "))
    r = None

    if choice == 1:
        r = client.connexion()
    elif choice == 2:
        r = client.register()
    elif choice == 3:
        r = client.quit_()
    else:
        pass

    if r is None:
        menu()
    else:
        game(r)


def game(sock):
    pass


menu()"""

import character.character as char
import map.map as map_
import gamelogic.mouseclicks as mouseclicks
import pyglet


window = pyglet.window.Window(1080, 720)
character = char.Character(0, 0)


@window.event
def on_mouse_release(x, y, button, modifiers):
    mouse_ = [x, y, button]
    if mouse_[2] == mouse.LEFT:
        mouseclicks.move_character(character)


@window.event
def on_draw():
    window.clear()
    map_.load_map()


def run():
    pyglet.app.run()


run()