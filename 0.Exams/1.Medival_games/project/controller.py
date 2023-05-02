class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

##############################################################################################3

    def __last_supply(self, supply_type):
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def __check_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    @staticmethod
    def __attack(p1, p2):
        p2.stamina -= (p1.stamina / 2)
        if p1.stamina - (p2.stamina / 2) < 0:
            p1.stamina = 0
        else:
            p1.stamina -= (p2.stamina / 2)
        if p1 < p2:
            return f"Winner: {p2.name}"
        else:
            return f"Winner: {p1.name}"

    @staticmethod
    def __check_players_for_duel(*players):
        result = []
        for player in players:
            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")
        if result:
            return "\n".join(result)

################################################################################################

    def add_player(self, *players):
        result = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                result.append(f"{player.name}")
        return f"Successfully added: {', '.join(result)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__check_player_by_name(player_name)
        if player.stamina == 100:
            return f"{player.name} have enough stamina."
        last_supply = self.__last_supply(sustenance_type)
        if last_supply:
            player._heal_player(last_supply)
            return f"{player_name} sustained successfully with {last_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__check_player_by_name(first_player_name)
        second_player = self.__check_player_by_name(second_player_name)
        result = self.__check_players_for_duel(first_player, second_player)
        if result:
            return result

        if first_player < second_player:
            return self.__attack(first_player, second_player)
        else:
            return self.__attack(second_player, first_player)

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)
        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(player.__str__())
        for supply in self.supplies:
            result.append(supply.details())
        return "\n".join(result)


