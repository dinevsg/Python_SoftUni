from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == "Unaffiliated" and player not in self.players:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

        elif player in self.players:
            return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name):
        for player_loc_data in self.players:
            if player_loc_data.name == player_name:
                self.players.remove(player_loc_data)
                player_loc_data.guild = "Unaffiliated"

                return f"Player {player_name} has been removed from the guild."

        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        for_print = "\n".join([p.player_info() for p in self.players])
        return f"Guild: {self.name}\n{for_print}"


# player = Player("George", 50, 100)
#
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
#
# guild = Guild("UGT")
#
# print(guild.assign_player(player))
# print(guild.guild_info())
