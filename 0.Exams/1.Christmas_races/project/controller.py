from project import MuscleCar
from project import SportsCar
from project import Driver
from project import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in ["MuscleCar", "SportsCar"]:
            return
        if model in [car.model for car in self.cars]:
            raise Exception(f"Car {model} is already created!")
        new_car = None
        if car_type == "MuscleCar":
            new_car = MuscleCar(model, speed_limit)
        elif car_type == "SportsCar":
            new_car = SportsCar(model, speed_limit)
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if driver_name in [driver.name for driver in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in [race.name for race in self.races]:
            raise Exception(f"Race {race_name} is already created!")
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

# ----------------------------------------------------------------------
    def __driver_search(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        raise Exception(f"Driver {driver_name} could not be found!")

    def __car_search(self, car_type):
        for car in reversed(self.cars):
            if not car.is_taken and car_type == car.__class__.__name__:
                return car
        raise Exception(f"Car {car_type} could not be found!")

    def __race_search(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        raise Exception(f"Race {race_name} could not be found!")

# ----------------------------------------------------------------------
    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__driver_search(driver_name)
        car = self.__car_search(car_type)
        if driver.car is not None:
            old_car = driver.car
            old_car.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."
        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__race_search(race_name)
        driver = self.__driver_search(driver_name)
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver_name in [driver.name for driver in race.drivers]:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__race_search(race_name)
        if race and len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        sorted_drivers = sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True)
        result = []
        for i, driver in enumerate(sorted_drivers, 1):
            if i <= 3:
                result.append(f"Driver {driver.name} wins the {race_name} "
                              f"race with a speed of {driver.car.speed_limit}.")
                driver.number_of_wins += 1
        return "\n".join(result)
