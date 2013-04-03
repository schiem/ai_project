class Monster:
    def __init__(health=100, name="Darkling", offbalance=False):
        self.health = health
        self.name = name
        self.offbalance = offbalance
    def attack(self):
        #calculate and return the best move
        return 'attack'        

    def take_damage(self, damage):
        self.health -= damage

