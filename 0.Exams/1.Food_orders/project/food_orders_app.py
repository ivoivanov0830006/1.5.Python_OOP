from project import Client


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 0

    def register_client(self, phone_number: str):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                raise Exception("The client has already been registered!")
        new_client = Client(phone_number)
        self.clients_list.append(new_client)
        return f"Client {phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if type(meal).__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        menu_details = []
        for meal in self.menu:
            menu_details.append(meal.details())
        return "\n".join(menu_details)

    def __check_if_client_is_registered(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return True

    def __find_client(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client

    def add_meals_to_shopping_cart(self, phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if not self.__check_if_client_is_registered(phone_number):
            self.register_client(phone_number)
        current_client = self.__find_client(phone_number)
        current_bill = 0
        current_meals = []

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_quantity:
                        current_meals.append(meal)
                        current_bill += meal_quantity * meal.price
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        current_client.shopping_cart.extend(current_meals)
        current_client.bill += current_bill

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            if meal_name not in current_client.ordered_meals:
                current_client.ordered_meals[meal_name] = 0
            current_client.ordered_meals[meal_name] += meal_quantity
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_quantity

        result = (meal.name for meal in current_client.shopping_cart)
        return f"Client {phone_number} successfully ordered {', '.join(result)} for {current_client.bill:.2f}lv."

    def cancel_order(self, phone_number: str):
        current_client = self.__find_client(phone_number)
        if len(current_client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        for ordered_meal, ordered_quantity in current_client.ordered_meals.items():
            for meal in self.menu:
                if ordered_meal == meal.name:
                    meal.quantity += ordered_quantity
        current_client.shopping_cart = []
        current_client.bill = 0
        current_client.ordered_meals = {}
        return f"Client {phone_number} successfully canceled his order."

    def finish_order(self, phone_number: str):
        current_client = self.__find_client(phone_number)
        if len(current_client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        total = current_client.bill
        current_client.shopping_cart = []
        current_client.bill = 0
        current_client.ordered_meals = {}
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total:.2f} was successfully paid for {phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
