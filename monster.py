import random
import ai
import pickle

class Monster:
    def __init__(self, health=50, name="Darkling", offbalance=False, description=""):
        self.health = health
        self.name = name
        self.offbalance = offbalance
        self.move = None
        self.history = []
        self.matches = 0
        self._load_history()

    def attack(self, moves, player):
        #calculate and return the best move
        move, self.matches = ai.best_move(player.history, self.history)
        if move is None:
            return random.choice(moves)
        move = ai.convert_to_opposing(move) 
        if (move == "attack" and self.offbalance is True):
            return random.choice(moves)
        return moves

    def take_damage(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health <= 0

    def save_history(self):
        if self.name.lower() != 'player':
            f = open('monster.moves', 'w+')
        else:
            f = open('player.moves', 'w+')
        pickle.dump(self.history, f)
        f.close()

    def _load_history(self):
        try:
            f = open(self.name + '.moves', 'r+')
            self.history = pickle.load(f)
            f.close()
        except Exception:
            pass
