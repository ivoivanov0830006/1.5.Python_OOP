class Rhombus:

    def __init__(self, size):
        self.size = size
        self.result = ''

    def main(self):
        self.upper_part()
        self.lower_part()
        return self.result

    def upper_part(self):
        for row in range(1, self.size + 1):
            self.draw_rhombus(row)

    def lower_part(self):
        for row in range(self.size - 1, 0, -1):
            self.draw_rhombus(row)

    def draw_rhombus(self, row):
        self.result += (' ' * (self.size - row)) + ('* ' * row) + '\n'


n = int(input())
rhombus = Rhombus(n).main()
print(rhombus)


"""
------------------------------------- Another Solution -----------------------------

def print_row(n, row):
    for space in range(n - row):
        print(" ", end="")
    for star in range(1, row):
        print("*", end=" ")
    print("*")


def print_upper(n):
    for row in range(1, n + 1):
        print_row(n, row)


def print_lower(n):
    for row in range(n - 1, 0, -1):
        print_row(n, row)


def print_rhombus(n):
    print_upper(n)
    print_lower(n)


n = int(input())
print_rhombus(n)
