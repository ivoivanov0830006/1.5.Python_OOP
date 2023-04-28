from project import Appaloosa
from project import HorseRace
from project import Thoroughbred
from project import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def __jockey_search(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return next(filter(lambda x: x.name == jockey_name, self.jockeys), None)
        raise Exception(f"Jockey {jockey_name} could not be found!")

    def __horse_search(self, horse_type):
        for horse in reversed(self.horses):
            if not horse.is_taken and horse_type == horse.__class__.__name__:
            # if not horse.is_taken and horse_type == type(horse).__name__:
                return horse
        raise Exception(f"Horse breed {horse_type} could not be found!")

    def __race_search(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        raise Exception(f"Race {race_type} could not be found!")

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in ["Appaloosa", "Thoroughbred"]:
            return
        if horse_name in [horse.name for horse in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")
        new_horse = None
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)
        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [jockey.name for jockey in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [horse_race.race_type for horse_race in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        current_jockey = self.__jockey_search(jockey_name)
        current_horse = self.__horse_search(horse_type)
        if current_jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        current_jockey.horse = current_horse
        current_horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {current_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        current_jockey = self.__jockey_search(jockey_name)
        current_race = self.__race_search(race_type)
        if not current_jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey_name in [jockey.name for jockey in current_race.jockeys]:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        current_race.jockeys.append(current_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        current_race = self.__race_search(race_type)
        if len(self.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        winner = sorted(current_race.jockeys, key=lambda jockey: jockey.horse.speed)[-1]
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! " \
               f"Winner's horse: {winner.horse.name}."
