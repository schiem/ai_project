from monster import Monster
from ui import UI

ACTION_QUIT = 'quit'

MOVE_ATTACK = 'attack'
MOVE_BASH = 'bash'
MOVE_DEFEND = 'defend'

moves = [MOVE_ATTACK, MOVE_BASH, MOVE_DEFEND]

action_table = { MOVE_ATTACK + MOVE_ATTACK : [1, False, 1, False], 
                 MOVE_ATTACK + MOVE_DEFEND : [0, True, 0, False], 
                 MOVE_ATTACK + MOVE_BASH : [0, False, 2, False],
                 MOVE_DEFEND + MOVE_DEFEND : [0, False, 0, False],
                 MOVE_DEFEND + MOVE_BASH : [1, True, 0, False],
                 MOVE_BASH + MOVE_BASH : [2, True, 2, True]
}

def run():
    player = Monster(100, 'temp_name')
    monster = Monster()
    ui = UI()

    ui.welcome()

    player.name = ui.player_name()

    player_move = "Run"
    while player_move.lower() != ACTION_QUIT:
        
        if player.offbalance:
            moves = [MOVE_BASH, MOVE_DEFEND]
        else:
            moves = [MOVE_ATTACK, MOVE_BASH, MOVE_DEFEND]
        player_move = ui.player_move(moves)
        
        if player_move == ACTION_QUIT:
            break
        if player_move not in moves:
            ui.display("I don't understand your input, try again.")
            continue
        
        monster_move = monster.attack()
        if player_move + monster_move in action_table:
            outcome = action_table[player_move + monster_move]
            monster.take_damage(outcome[2])
            monster.offbalance = outcome[3]
            player.take_damage(outcome[0])
            player.offbalance = outcome[1]
        else:
            outcome = action_table[monster_move + player_move]
            monster.take_damage(outcome[0])
            monster.offbalance = outcome[1]
            player.take_damage(outcome[2])
            player.offbalance = outcome[3]

        print "Your health is " + str(player.health)
        if player.offbalance:
            print "You are offbalance"
        print "Monster health is " + str(monster.health)
        if monster.offbalance:
            print "Monster is offblanace"
        #check_if_dead()
