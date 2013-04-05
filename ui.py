class UI:
    def welcome(self):
        self.display("Welcome to the MUD!\n\nAt any time you may type 'quit' (without the quotes) to stop playing.")

    def player_name(self):
        return self.user_input("What do you want your character's name to be?")

    def player_move(self, moves):

        msg = "How do you want to move?\nYour options are: "

        for name in moves:
            msg += "\n\t" + name.capitalize()

        return self.user_input(msg + "\nYour move").lower()

    def display(self, msg):
        print(msg)

    def user_input(self, msg):
        return raw_input(msg + ": ")

    def display_status(self, player, monster):
        self.display("Your health is " + str(player.health))
        if player.offbalance:
           self.display("You are offbalance")
        self.display("Monster health is " + str(monster.health))
        if monster.offbalance:
            self.display("Monster is offblanace")
