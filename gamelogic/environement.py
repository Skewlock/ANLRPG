class Game:
    # 0 : fermeture du jeu
    # 1 : exploration
    # 2 : combat
    def __init__(self):
        self.state = 1
        # définir le mode de mouvement utilisé
        
    def change_state(self, state):
        self.state = state
        # changer le mouvement