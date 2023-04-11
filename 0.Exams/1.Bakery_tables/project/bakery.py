from project import Bread
from project import Cake
from project import Tea
from project import Water
from project import InsideTable
from project import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def __check_food(self, name):
        for food in self.food_menu:
            if food.name == name:
                return food

    def __check_drink(self, name):
        for drink in self.drinks_menu:
            if drink.name == name:
                return drink

    def __check_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def add_food(self, food_type: str, name: str, price: float):
        if food_type in ["Bread", "Cake"]:
            food = self.__check_food(name)
            if food:
                raise Exception(f"{food_type} {name} is already in the menu!")
            if food_type == "Bread":
                new_food = Bread(name, price)
                self.food_menu.append(new_food)
            elif food_type == "Cake":
                new_food = Cake(name, price)
                self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type in ["Tea", "Water"]:
            drink = self.__check_drink(name)
            if drink:
                raise Exception(f"{drink_type} {name} is already in the menu!")
            if drink_type == "Tea":
                new_drink = Tea(name, portion, brand)
                self.drinks_menu.append(new_drink)
            elif drink_type == "Water":
                new_drink = Water(name, portion, brand)
                self.drinks_menu.append(new_drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type in ["InsideTable", "OutsideTable"]:
            table = self.__check_table(table_number)
            if table:
                raise Exception(f"Table {table_number} is already in the bakery!")
            if table_type == "InsideTable":
                new_table = InsideTable(table_number, capacity)
                self.tables_repository.append(new_table)
            elif table_type == "OutsideTable":
                new_table = OutsideTable(table_number, capacity)
                self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.__check_table(table_number)
        if not table:
            return f"Could not find table {table_number}"
        food_in_menu = []
        food_not_in_menu = []
        for food_name in food_names:
            food = self.__check_food(food_name)
            if food:
                food_in_menu.append(food.__repr__())
                table.food_orders.append(food)
            else:
                food_not_in_menu.append(food_name)
        result = [f"Table {table_number} ordered:", *food_in_menu,
                  f"{self.name} does not have in the menu:", *food_not_in_menu]
        return "\n".join(result)

    def order_drink(self, table_number: int, *drinks_names):
        table = self.__check_table(table_number)
        if not table:
            return f"Could not find table {table_number}"
        drinks_in_menu = []
        drinks_not_in_menu = []
        for drink_name in drinks_names:
            drink = self.__check_food(drink_name)
            if drink:
                drinks_in_menu.append(drink.__repr__())
                table.drink_orders.append(drink)
            else:
                drinks_not_in_menu.append(drink_name)
        result = [f"Table {table_number} ordered:", *drinks_in_menu,
                  f"{self.name} does not have in the menu:", *drinks_not_in_menu]
        return "\n".join(result)

    def leave_table(self, table_number: int):
        table = self.__check_table(table_number)
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        result = [f"Table: {table_number}",
                  f"Bill: {table_bill:.2f}"]
        return "\n".join(result)

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            if not table.is_reserved:
                result.append(table.free_table_info())
        return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"


