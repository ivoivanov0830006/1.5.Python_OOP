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

    def create_band(self, name: str):
        band = self.__find_band(name)
        if band:
            raise Exception(f"{name} band is already created!")
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.__find_concert(place)
        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.__find_musician(musician_name)
        band = self.__find_band(band_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.__find_band(band_name)
        musician = None
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        for current_musician in band.members:
            if current_musician.name == musician_name:
                musician = current_musician
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        guitar_count = 0
        sing_count = 0
        drum_count = 0
        band = self.__find_band(band_name)
        concert = self.__find_concert(concert_place)
        for member in band.members:
            if member.__class__.__name__ == "Guitarist":
                guitar_count += 1
            elif member.__class__.__name__ == "Drummer":
                drum_count += 1
            elif member.__class__.__name__ == "Singer":
                sing_count += 1
        if guitar_count < 1 or sing_count < 1 or drum_count < 1:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Singer" and "sing high pitch notes" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Guitarist" and "play rock" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Metal":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Singer" and "sing low pitch notes" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Guitarist" and "play metal" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Jazz":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drum brushes" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Singer" and ("sing low pitch notes" not in member.skills or
                                                              "sing high pitch notes" not in member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if member.__class__.__name__ == "Guitarist" and "play jazz" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
