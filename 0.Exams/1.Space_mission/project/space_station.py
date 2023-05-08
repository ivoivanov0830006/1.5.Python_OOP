from project import Biologist
from project import Geodesist
from project import Meteorologist
from project import Planet
from project import PlanetRepository
from project import AstronautRepository


class SpaceStation:
    COMPLETED_MISSIONS = 0
    FAILED_MISSIONS = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")
        else:
            if astronaut_type == "Biologist":
                new_astronaut = Biologist(name)
                self.astronaut_repository.add(new_astronaut)
            elif astronaut_type == "Geodesist":
                new_astronaut = Geodesist(name)
                self.astronaut_repository.add(new_astronaut)
            elif astronaut_type == "Meteorologist":
                new_astronaut = Meteorologist(name)
                self.astronaut_repository.add(new_astronaut)
            return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        new_planet = Planet(name)
        new_planet.items = items.split(", ")
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception(f'Invalid planet name!')
        sorted_astronauts = sorted(self.astronaut_repository.astronauts, key=lambda x: x.oxygen, reverse=True)
        suitable_astronauts = []
        for i, astronaut in enumerate(sorted_astronauts, 1):
            if i <= 5 and astronaut.oxygen > 30:
                suitable_astronauts.append(astronaut)
        if not suitable_astronauts:
            raise Exception(f'You need at least one astronaut to explore the planet!')
        for i, astronaut in enumerate(suitable_astronauts, 1):
            while astronaut.oxygen > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
                if not planet.items:
                    self.COMPLETED_MISSIONS += 1
                    return f'Planet: {planet_name} was explored. {i} ' \
                           f'astronauts participated in collecting items.'
        self.FAILED_MISSIONS += 1
        return f'Mission is not completed.'

    def report(self):
        result = [f"{self.COMPLETED_MISSIONS} successful missions!",
                  f"{self.FAILED_MISSIONS} missions were not completed!", "Astronauts' info:"]
        all_astronauts = self.astronaut_repository.astronauts
        for astronaut in all_astronauts:
            result.append(f"Name: {astronaut.name}")
            result.append(f"Oxygen: {astronaut.oxygen}")
            if len(astronaut.backpack) == 0:
                result.append("Backpack items: none")
            else:
                result.append(f"Backpack items: {', '.join(astronaut.backpack)}")
        return "\n".join(result)
