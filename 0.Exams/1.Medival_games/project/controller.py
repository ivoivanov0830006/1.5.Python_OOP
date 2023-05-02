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
