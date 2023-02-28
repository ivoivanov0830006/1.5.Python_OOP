class Glass:
    """This is class Glass with class attribute capacity"""
    capacity = 250

    def __init__(self):
        """This is instance attribute"""
        self.content = 0

    def fill(self, ml):
        space_left = Glass.capacity - self.content
        if space_left >= ml:
            self.content += ml
            return f"Glass filled with {ml} ml"

        return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        space_left = Glass.capacity - self.content
        return f"{space_left} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
print(glass.__doc__)
