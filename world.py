from monster import Monster
from ui import UI

ACTION_QUIT = 'quit'

MOVE_ATTACK = 'attack'
MOVE_BLOCK = 'block'

moves = [MOVE_ATTACK, MOVE_BLOCK]

def run():
    player = Monster(100, 'temp_name')
    ui = UI()

    ui.welcome()

    player.name = ui.player_name()

    player_move = "Run"
    while player_move.lower() != ACTION_QUIT:

        player_move = ui.player_move()

        if player_move not in moves and player_move != ACTION_QUIT:
            ui.display("I don't understand your input, try again.")
            continue

        #monster_move = monster.attack()
        #monster.do_action(player_move, monster_move)
        #check_if_dead()
