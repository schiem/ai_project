class UI:
    def welcome(self):
        self.display("Welcome to the MUD!\n\nAt any time you may type 'quit' (without the quotes) to stop playing.")

    def player_name(self):
        return self.user_input("What do you want your character's name to be?")

    def player_move(self):
        from world import moves

        msg = "How do you want to move?\nYour options are: "

        for name in moves:
            msg += "\n\t" + name.capitalize()

        return self.user_input(msg + "\nYour move").lower()

    def display(self, msg):
        print(msg)

    def user_input(self, msg):
        return input(msg + ": ")
