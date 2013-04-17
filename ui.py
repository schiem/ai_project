try:
    eval("print('test')")
except SyntaxError:
    from compat import *

class UI:
    def __init__(self, player):
        self.player = player
        self.monster = None
        self.msg = ""

    def welcome(self):
        self.display("Welcome to the MUD!\n\nAt any time you may type 'quit' (without the quotes) to stop playing.")

    def player_move(self, moves):
        msg = "How do you want to move?\nYour options are: "

        for name in moves:
            msg += "\n\t" + name.capitalize()

        return self.user_input(msg + "\nYour move").lower()

    def display_status(self, player, monster):
        msg = "Health: " + str(player.health) + " "
        if player.offbalance:
          msg += "(You are offbalance) "
        msg += monster.name + " health: " + str(monster.health) + " "
        if monster.offbalance:
            msg += "(Monster is offblanace)"
        self.display(msg)

    def display(self, msg):
        from sys import stdout
        stdout.write(msg + "\n")

    def user_input(self, msg):
        return input(msg + ": ")

    def update_display(self):
        print chr(27) + "[2J"
        self.display_status(self.player, self.monster)
        self.display("You " + self.player.move + "ed")
        self.display(self.monster.name + " " + self.monster.move + "ed")
