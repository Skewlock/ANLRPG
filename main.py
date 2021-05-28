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
import gamelogic.environement as env
import gamelogic.mouseclicks as mouseclicks
import fight.ennemies as ennemies
import pyglet
import pyglet.window.mouse as mouse

window = pyglet.window.Window(1080, 720)  # la fenêtre de pyglet
character = char.Character(0, 0)  # le personnage (déclaré ici mais peut changer)
john = ennemies.John(1, 10, 1, 0)
#morsure = Morsure("Morsure", 1, 2, 1)
global game
game = env.Game()
game.change_state(2, character, john)


@window.event
def on_mouse_release(x, y, button, modifiers):  # tout ce qui est lié à la souris
    mouse_ = [x, y, button]  # on crée une liste d'argument de la souris
    if mouse_[2] == mouse.LEFT:  # si on clic gauche
        if character.casting:
            character.get_target(mouseclicks.get_coords_grid())
        mouseclicks.move_character(character, mouse_, window, john)  # on déplace le personnage


@window.event
def on_draw():  # chaque frame sera gérée ici (d'abord clear puis dessinée encore)
    window.clear()
    map_.load_map(window)
    character.draw(window)
    john.draw(window)
    map_.load_decors(window)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.E:
        character.cast_spell()


def run():  # on lance le jeu
    pyglet.app.run()


run()
