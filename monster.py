import random

class Monster:
    def __init__(self, health=10, name="Darkling", offbalance=False):
        self.health = health
        self.name = name
        self.offbalance = offbalance
    def attack(self, moves):
        #calculate and return the best move
        return random.choice(moves)

    def take_damage(self, damage):
        self.health -= damage

