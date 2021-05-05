import networking.client as client


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


menu()