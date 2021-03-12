import socket
import threading
import sqlite3


# on déclare le thread pour chaque client
class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip # ip du client
        self.port = port # port de com
        self.clientsocket = clientsocket # assez explicite là...
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

    def run(self):
        print("Connexion de %s %s" % (self.ip, self.port,))
        r = self.clientsocket.recv(1024) # réception du paquet du client
        text = str(r, "utf-8") # conversion en texte
        command = text.split(":")[0] # récupération de la commande
        args = text.split(":")[1:] # récupération des arguments
        print("[!] Command recieved :")
        print("command: "+ command)
        print("args: "+str(args))
        print("-------------")
        # dictionnaire des commandes
        comm = {
            "register": self.register,
            "login": self.login
            }
        # exécute la commande
        fnc = comm.get(command)
        fnc(args)
    
    def login(self, args): # commande login
        if len(args) == 2: # si assez d'arguments fournis
            try:
                db = sqlite3.connect("db.db")
                cursor = db.cursor()
                cursor.execute("SELECT password FROM users WHERE login=?",(args[0],)) # récupère le password
                pass_ = cursor.fetchone()
                db.close()
                if pass_[0] == args[1]: # si les deux passwords correspondent
                    print("valid login for %s %s" % (self.ip, self.port))
                    paquet = "valid_login"
                    self.clientsocket.send(paquet.encode("utf-8")) # on renvoie le paquet au client pour valider le pass
                else:
                    print("invalid credentials for %s %s" % (self.ip, self.port))
                    paquet = "invalid_credentials"
                    self.clientsocket.send(paquet.encode("utf-8")) # on renvoie le paquet d'erreur
            except TypeError:
                print("invalid credentials for %s %s" % (self.ip, self.port))
                paquet = "invalid_credentials"
                self.clientsocket.send(paquet.encode("utf-8")) #paquet d'erreur
        else: # s'il manque un arg, fait rien
            return
    
    def register(self, args):
        if len(args) == 2: # si assez d'args
            print("login :"+ args[0])
            print("password: "+args[1])
            try:
                db = sqlite3.connect("db.db")
                cursor = db.cursor()
                # ajoute les crédentials à la db
                cursor.execute("INSERT INTO users(login, password) VALUES(?,?)", (args[0], args[1]))
                db.commit()
                db.close()
            except: # si erreur
                print("error for  %s %s" % (self.ip, self.port))
                paquet = "error"
                self.clientsocket.send(paquet.encode("utf-8")) # renvoie le paquet d'erreur
            else:
                print("added account for %s %s" % (self.ip, self.port))
                paquet = "account_added"
                self.clientsocket.send(paquet.encode("utf-8")) # renvoie le paquet de réussite
        else:
            return


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 1000))
sock.listen(0) # accepte les connexions des sockets
while True:
    print("Listening...")
    # accept les sockets et fais un thread par client
    (clientsocket, (ip, port)) = sock.accept()
    client = ClientThread(ip, port, clientsocket)
    client.start()
