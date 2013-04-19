import world

def best_move(player_history, monster_history):
   player_pattern = player_history[-4:]
   pattern_list = instances_of(player_pattern, player_history[:-4])

   if len(pattern_list) == 0:
       player_pattern = player_history[-3:]
       pattern_list = instances_of(player_pattern, player_history[:-3])
   
   if len(pattern_list) > 0:
       moves = compare_monster(pattern_list, player_pattern, monster_history)
       if len(moves) > 0:
           matches = len(moves)
           return most_common(moves), matches
       else:
           moves = compare_monster(pattern_list, player_pattern, player_history)
           matches = len(moves)
           return most_common(moves), matches

   return None, 0


def most_common(lst):
    return max(set(lst), key=lst.count)

def instances_of(a, b):
    indices = []
    i = 0
    while i < len(b):
        if a == b[i:i+len(a)]:
            indices.append(i)
            i += len(a)
        else:
            i += 1
    return indices

def compare_monster(pattern_indices, player_pattern, monster_history):
    matches = []
    for i in pattern_indices:
        if player_pattern == monster_history[i:i + len(player_pattern)] and len(monster_history) >= len(player_pattern) + i - 1: 
            matches.append(monster_history[i + len(player_pattern)])
    return matches

def convert_to_opposing(move):
   return world.opposing_moves[move] 
