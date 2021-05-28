class Game:
    # 0 : fermeture du jeu
    # 1 : exploration
    # 2 : combat
    def __init__(self):
        self.state = 2
        # définir le mode de mouvement utilisé
        
    def change_state(self, state, character, ennemy):
        self.state = state
        if self.state == 2:
            self.create_fight_map(character, ennemy)
        # changer le mouvement
    
    def create_fight_map(self, character, ennemy):
        # 0: espace libre
        # 1: personnage
        # 2: ennemi
        self.map = [[0 for i in range(10)] for i in range(10)]
        self.map[character.x][character.y] = 1
        self.map[ennemy.x][ennemy.y] = 2