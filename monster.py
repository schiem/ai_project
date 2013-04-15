import random
import ai

class Monster:
    def __init__(self, health=50, name="Darkling", offbalance=False):
        self.health = health
        self.name = name
        self.offbalance = offbalance
        self.history = []

    def attack(self, moves, player):
        #calculate and return the best move
        move = ai.best_move(player.history, self.history)
        
        if move is None:
            return random.choice(moves)
        move = ai.convert_to_opposing(move) 
        return move

    def take_damage(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health <= 0
