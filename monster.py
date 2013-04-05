class Monster:
    def __init__(self, health=10, name="Darkling", offbalance=False):
        self.health = health
        self.name = name
        self.offbalance = offbalance
    def attack(self):
        #calculate and return the best move
        return 'defend'        

    def take_damage(self, damage):
        self.health -= damage

