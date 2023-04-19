from project import Band
from project import Drummer
from project import Guitarist
from project import Singer
from project import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def __find_musician(self, name):
        for musician in self.musicians:
            if musician.name == name:
                return musician

    def __find_band(self, name):
        for band in self.bands:
            if band.name == name:
                return band

    def __find_concert(self, place):
        for concert in self.concerts:
            if concert.place == place:
                return concert

    def create_musician(self, musician_type: str, name: str, age: int):
        musician = self.__find_musician(name)
        if musician:
            raise Exception(f"{name} is already a musician!")
        if musician_type not in ["Guitarist", "Drummer", "Singer"]:
            raise ValueError("Invalid musician type!")
        if musician_type == "Guitarist":
            new_musician = Guitarist(name, age)
            self.musicians.append(new_musician)
        elif musician_type == "Drummer":
            new_musician = Drummer(name, age)
            self.musicians.append(new_musician)
        elif musician_type == "Singer":
            new_musician = Singer(name, age)
            self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."
