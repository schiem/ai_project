from monster import Monster
from ui import UI
import random
ACTION_QUIT = 'quit'

MOVE_ATTACK = 'attack'
MOVE_BASH = 'bash'
MOVE_DEFEND = 'defend'

moves = [MOVE_ATTACK, MOVE_BASH, MOVE_DEFEND]
monster_moves = [MOVE_ATTACK, MOVE_BASH, MOVE_DEFEND]
action_table = { MOVE_ATTACK + MOVE_ATTACK : [1, False, 1, False],
                 MOVE_ATTACK + MOVE_DEFEND : [0, True, 0, False],
                 MOVE_ATTACK + MOVE_BASH : [0, False, 2, False],
                 MOVE_DEFEND + MOVE_DEFEND : [0, False, 0, False],
                 MOVE_DEFEND + MOVE_BASH : [1, True, 0, False],
                 MOVE_BASH + MOVE_BASH : [2, False, 2, False]
}

opposing_moves = {"attack" : "defend", "bash" : "attack", "defend" : "bash"}
monsters = {"Darkling" : [20, "A foul creature spawned of darkness.  It is adorned with razor sharp teeth and long claws."], "Orc" : [50, "A large, greenbeast, this humanoid figure knows nothing but violence."], "Lich" : [100, "A powerful undead creature, created from an ancient ritual.  Best be wary."]}


class World:
    def run(self):
        self.player = Monster(name='Player')

        monster = random.choice(list(monsters.viewkeys()))
        self.monster = Monster(monsters[monster][0], monster, description=monsters[monster][1])
        self.ui = UI(self.player)
        self.ui.monster = self.monster

        self.ui.welcome()
        
        a = 1
        while a != 0:
            a = self.run_loop()
            self.ui.update_display()

            self.monster.save_history()
            self.player.save_history()
            
            monster = random.choice(list(monsters.viewkeys()))
            self.monster = Monster(monsters[monster][0], monster, description=monsters[monster][1])
            self.ui.monster = self.monster

    def run_loop(self):
        player_move = "Run"
        while player_move.lower() != ACTION_QUIT:

            if self.player.offbalance:
                moves = [MOVE_BASH, MOVE_DEFEND]
            else:
                moves = [MOVE_ATTACK, MOVE_BASH, MOVE_DEFEND]
            if self.monster.offbalance:
                monster_moves = [MOVE_BASH, MOVE_DEFEND]
            else:
                monster_moves = [MOVE_ATTACK, MOVE_BASH, MOVE_DEFEND]

            player_move = self.ui.player_move(moves)

            if player_move == ACTION_QUIT:
                break
            if player_move not in moves:
                self.ui.msg = "I don't understand your input, try again."
                self.ui.update_display()
                continue

            monster_move = self.monster.attack(monster_moves, self.player)
            
            self.ui.monster.move = monster_move
            self.ui.player.move = player_move

            if player_move + monster_move in action_table:
                outcome = action_table[player_move + monster_move]
                self.monster.take_damage(outcome[2])
                self.monster.offbalance = outcome[3]
                self.player.take_damage(outcome[0])
                self.player.offbalance = outcome[1]
            else:
                outcome = action_table[monster_move + player_move]
                self.monster.take_damage(outcome[0])
                self.monster.offbalance = outcome[1]
                self.player.take_damage(outcome[2])
                self.player.offbalance = outcome[3]

            # record the moves just made for the AI
            self.player.history.append(player_move)
            self.monster.history.append(monster_move)

            self.ui.update_display()

            if self.player.is_dead() and self.monster.is_dead():
                self.ui.msg = "You have slain the foul " + self.monster.name + ", but it appears that, in its dying throes, the " + self.monster.name + "has also slain you."
                return 0
            elif self.player.is_dead():
                self.ui.msg = "Oh no! You seem to have perished!"
                return 0
            elif self.monster.is_dead():
                self.ui.msg = "You have slain the " + self.monster.name + "."
                return 1
        return 0
