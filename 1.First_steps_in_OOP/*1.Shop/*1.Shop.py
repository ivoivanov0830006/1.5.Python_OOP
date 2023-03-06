class Shop:
    def __init__(self, name, items):
        self.name = str(name)
        self.items = items

    def get_items_count(self):
        result = len(self.items)
        return result


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())


"""
------------------------------------ Problem to resolve --------------------------------

Create a class called Shop. Upon initialization, it should receive a name (string) and items 
(list). Create a method called get_items_count() which should return the number of items in the store.
-------------------------------------- Example inputs ----------------------------------
Test Code	
shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())	
Output
3

"""
