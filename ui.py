class UI:
    def __init__(self, player):
        self.player = player

        self._setup_player()

    def _setup_player(self):
        self.player.name = input("Please input your character name:")

    def player_move(self):
        return raw_input("How do you want to move?\nYour options are:\n\t1) Block\n\t2) Fight\n\nYour move: ")
