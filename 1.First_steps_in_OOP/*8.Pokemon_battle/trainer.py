from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon_list = []

    def add_pokemon(self, new_pokemon: Pokemon):
        if new_pokemon not in self.pokemon_list:
            self.pokemon_list.append(new_pokemon)
            return f"Caught {new_pokemon.pokemon_details()}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, searched_pokemon):
        for pok in self.pokemon_list:
            if pok.name == searched_pokemon:
                self.pokemon_list.remove(pok)
                return f"You have released {searched_pokemon}"

        return "Pokemon is not caught"

    def trainer_data(self):
        result = ""
        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemon_list)}\n"
        for item in self.pokemon_list:
            result += f"- {item.pokemon_details()}\n"
        return result


