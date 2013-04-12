def best_move(player_history=None, monster_history=None):
   if len(player_history) > 4:
       pattern_list = isin(player_history[:-4], player_history[-4:])
       if len(pattern_list) == 0:
           pattern_list = isin(player_history[:-3], player_history[-3:])
       if len(pattern_list) == 0:
           return None
       moves = compare_monster(pattern_list, monster_history)
       return most_common(moves)
   else:
       return None


def most_common(lst):
    return max(set(lst), key=lst.count)

    
