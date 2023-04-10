from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str, capacity: int = 15):
        super().__init__(name, capacity)

    def details(self):
        robot_names = []
        result = [f"{self.name} Secondary Service:"]
        if self.robots:
            for robot in self.robots:
                robot_names.append(robot.name)
            result.append(f"Robots: {' '.join(robot_names)}")
        else:
            result.append("Robots: none")
        return "\n".join(result)
