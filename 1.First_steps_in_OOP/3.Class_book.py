class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)


"""
------------------------------------ Problem to resolve --------------------------------

Create a class called Book. It should have an __init__() method that should receive:
        name: string
        author: string
        pages: int
-------------------------------------- Example inputs ----------------------------------
Test Code	
book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)	
Output
My Book
Me
200

"""
