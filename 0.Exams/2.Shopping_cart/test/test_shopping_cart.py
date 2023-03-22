from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self):
        self.shop = ShoppingCart("Lidl", 100)

    def test_correct_initializing(self):
        self.assertEqual("Lidl", self.shop.shop_name)
        self.assertEqual(100, self.shop.budget)

    def test_invalid_shop_name_raise_ex(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.shop_name = "lidl2"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_product_with_invalid_price_raise_ex(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_to_cart("Tomato", 100)
        self.assertEqual(f"Product Tomato cost too much!", str(ve.exception))

    def test_add_to_cart_product_with_valid_price(self):
        result = self.shop.add_to_cart("Tomato", 99)
        self.assertEqual("Tomato product was successfully added to the cart!", result)
        self.assertEqual(self.shop.products, {"Tomato": 99})

    def test_remove_from_cart_invalid_product_raise_ex(self):
        self.shop.products = {"Potato": 20,
                              "Oregano": 10}
        with self.assertRaises(ValueError) as ve:
            self.shop.remove_from_cart("Tomato")
        self.assertEqual("No product with name Tomato in the cart!", str(ve.exception))

    def test_remove_from_cart_valid_product(self):
        self.shop.products = {"Tomato": 20,
                              "Oregano": 10}
        result = self.shop.remove_from_cart("Tomato")
        self.assertEqual("Product Tomato was successfully removed from the cart!", result)
        self.assertEqual(self.shop.products, {"Oregano": 10})

    def test_add_another_shopping_cart_method(self):
        shop1 = ShoppingCart("Lidl", 500)
        shop1.add_to_cart("Lidl-tomato", 3)
        shop2 = ShoppingCart("Kaufland", 100)
        shop2.add_to_cart("Kaufland-potato", 4)
        result = shop1.__add__(shop2)
        self.assertEqual("LidlKaufland", result.shop_name)
        self.assertEqual(600, result.budget)
        self.assertEqual({"Lidl-tomato": 3, "Kaufland-potato": 4}, result.products)

    def test_buy_products_invalid_total_raise_ex(self):
        self.shop.products = {"Tomato": 60, "Potato": 70}
        with self.assertRaises(ValueError) as ve:
            self.shop.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 30.00lv!", str(ve.exception))

    def test_buy_products_valid_total(self):
        self.shop.products = {"Tomato": 60, "Potato": 30}
        result = self.shop.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 90.00lv.", result)


if __name__ == "__main__":
    main()
