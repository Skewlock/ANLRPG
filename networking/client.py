import socket
import threading
# import hashlib

# class ThreadServer(threading.Thread):

ip_server = "127.0.0.1"
port = 1000

sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip_server, port))

def menu():
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


def connexion():
    login = input("login: ")
    password = input("password: ")
    paquet = "login:"+login+":"+password
    sock.send(paquet.encode("utf-8"))
    menu()


def register():
    login = input("Quel est votre login: ")
    password = input("Quel est votre password: ")
    confirm = input("Confirmez votre mot de passe: ")
    
    if confirm == password:
        paquet = "register:"+login+":"+password
        sock.send(paquet.encode("utf-8"))
        print("Votre compte a été enregistré.")
    else:
        print("Les mots de passe ne matchent pas.")
    menu()


def quit_():
    sock.close()
    quit()

menu()