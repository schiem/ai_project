from monster import Monster
from ui import UI

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

class World:
    def run(self):
        self.player = Monster(name='Player')
        self.monster = Monster()
        self.ui = UI()

        print chr(27) + "[2J"
        self.ui.welcome()

        a = 1
        while a != 0:
            self.monster = Monster()
            a = self.run_loop()

            self.monster.save_history()
            self.player.save_history()


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
                self.ui.display("I don't understand your input, try again.")
                continue

            monster_move = self.monster.attack(monster_moves, self.player)
            
            self.ui.display(self.monster.name + " move: " + monster_move)
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

            # record the moves just made
            self.player.history.append(player_move)
            self.monster.history.append(monster_move)

            print chr(27) + "[2J"
            self.ui.display_status(self.player, self.monster)
            if self.player.is_dead() and self.monster.is_dead():
                self.ui.display("You have slain the foul " + self.monster.name + ", but it appears that, in its dying throes, the " + self.monster.name + "has also slain you.")
                return 0
            elif self.player.is_dead():
                self.ui.display("Oh no! You seem to have perished!")
                return 0
            elif self.monster.is_dead():
                self.ui.display("You have slain the " + self.monster.name + ".")
                return 1
        return 0
