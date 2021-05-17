class Ennemy:
    
    def __init__(self, hp, mp, pm):
        self.hp = hp
        self.mana = mp
        self.pm = pm
    
    def move(self):
        # déplacement du sprite et des ennemis
        pass
    

class John(Ennemy):
    
    def __init__(self, hp, mp, pm, ar):
        Ennemy.__init__(hp, mp, pm)
        self.armure = ar
    
    def take_damage(self, damage):
            self.hp -= (damage - armure)