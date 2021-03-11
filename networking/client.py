import socket
import threading

# class ThreadServer(threading.Thread):

ip_server = "127.0.0.1"
port = 1000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip_server, port))


def menu():  # menu dans la console
    print("-------------------------------------")
    print("\t[Menu de connexion]")
    print("[1]: Connexion")
    print("[2]: Register")
    print("[3]: Quitter")
    print("-------------------------------------")
    choice = int(input("Votre choix: "))

    if choice == 1:
        connexion()
    elif choice == 2:
        register()
    elif choice == 3:
        quit_()
    else:
        pass


def connexion():  # fonction de connexion
    login = input("login: ")
    password = input("password: ")
    paquet = "login:" + login + ":" + password  # crée le paquet avec login et password
    sock.send(paquet.encode("utf-8"))  # envoie le paquet
    r = sock.recv(1024)  # attends une réponse
    if str(r, "utf-8") == "valid_login":  # si le login est bon
        print("Mot de passe correct !")
    else:
        print("Login ou Mot de passe incorrect !")
    menu()  # recall le menu


def register():  # créer un compte
    login = input("Quel est votre login: ")
    password = input("Quel est votre password: ")
    confirm = input("Confirmez votre mot de passe: ")

    if confirm == password:  # si la confirmation du pass est bonne
        paquet = "register:" + login + ":" + password  # prépare le paquet
        sock.send(paquet.encode("utf-8"))  # envoie le paquet
        print("Votre compte a été enregistré.")
    else:
        print("Les mots de passe ne matchent pas.")
    menu()  # rappelle le menu


def quit_():  # fermer le socket et le programme
    sock.close()
    quit()


menu()
