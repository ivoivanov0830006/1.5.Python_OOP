from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    @staticmethod
    def __find_robot_in_service(robot_name, service):
        for robot in service.robots:
            if robot.name == robot_name:
                return robot

    def add_service(self, service_type: str, name: str):
        if service_type not in ["MainService", "SecondaryService"]:
            raise Exception("Invalid service type!")
        if service_type == "MainService":
            new_service = MainService(name)
            self.services.append(new_service)
            return f"{service_type} is successfully added."
        if service_type == "SecondaryService":
            new_service = SecondaryService(name)
            self.services.append(new_service)
            return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in ["MaleRobot", "FemaleRobot"]:
            raise Exception("Invalid robot type!")
        if robot_type == "MaleRobot":
            new_robot = MaleRobot(name, kind, price)
            self.robots.append(new_robot)
            return f"{robot_type} is successfully added."
        if robot_type == "FemaleRobot":
            new_robot = FemaleRobot(name, kind, price)
            self.robots.append(new_robot)
            return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(filter(lambda x: x.name == robot_name, self.robots), None)
        service = next(filter(lambda x: x.name == service_name, self.services), None)
        if (type(robot).__name__ == "FemaleRobot" and type(service).__name__ == "MainService") or \
                (type(robot).__name__ == "MaleRobot" and type(service).__name__ == "SecondaryService"):
            return "Unsuitable service."
        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")
        service.robots.append(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(filter(lambda x: x.name == service_name, self.services), None)
        robot = self.__find_robot_in_service(robot_name, service)
        if not robot:
            raise Exception("No such robot in this service!")
        self.robots.append(robot)
        service.robots.remove(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next(filter(lambda x: x.name == service_name, self.services), None)
        for robot in service.robots:
            robot.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = next(filter(lambda x: x.name == service_name, self.services), None)
        total_price = 0
        for robot in service.robots:
            total_price += robot.price
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(str(service.details()))
        return '\n'.join(result)
