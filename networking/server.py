import socket
import threading
import sqlite3


class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

    def run(self):
        print("Connexion de %s %s\n" % (self.ip, self.port,))
        r = self.clientsocket.recv(1024)
        text = str(r, "utf-8")
        command = text.split(":")[0]
        args = text.split(":")[1:]
        print("command: "+ command)
        print("args: "+str(args))
        comm = {
            "register": self.register,
            "login": self.login
            }
        fnc = comm.get(command, lambda: "Commande invalide")
        fnc(args)
    
    def login(self, args):
        if len(args) == 2:
            print("login: ", args[0])
            print("password: ", args[1])
            try:
                db = sqlite3.connect("db.db")
                cursor = db.cursor()
                cursor.execute("SELECT password FROM users WHERE login=?",(args[0],))
                pass_ = cursor.fetchone()
                db.commit()
                db.close()
                if pass_[0] == args[1]:
                    print("le mot de passe est le même")
                else:
                    print("mot de passe différent")
            except TypeError:
                print("Le login n'existe pas")
        else:
            return
    
    def register(self, args):
        if len(args) == 2:
            # print("registering "+ self.ip+" "+ self.port)
            print("login :"+ args[0])
            print("password: "+args[1])
            try:
                db = sqlite3.connect("db.db")
                cursor = db.cursor()
                cursor.execute("INSERT INTO users(login, password) VALUES(?,?)", (args[0], args[1]))
                db.commit()
                db.close()
            except:
                print("Une erreur a eu lieu")
        else:
            return


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 1000))
sock.listen(0)
while True:
    print("Listening...")
    (clientsocket, (ip, port)) = sock.accept()
    client = ClientThread(ip, port, clientsocket)
    client.start()
