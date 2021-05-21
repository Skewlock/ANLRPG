class Spell:
    # types :
        # 1: sort de dégâts classique
        # 2: sort de zone
        # 3: glyphe
        # 4: pièges
    def __init__(self, name="undefined", t=1, d=0, r=1):
        self.name = name
        self.type = t
        self.damages = d
        self.range = r
    

class Morsure(Spell):
    
    def __init__(self, n, t, d, r):
        Spell.__init__(n,t,d,r)
        