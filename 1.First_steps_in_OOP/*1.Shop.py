class Shop:
    def __init__(self, name, items):
        self.name = str(name)
        self.items = items

    def get_items_count(self):
        result = len(self.items)
        return result


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
