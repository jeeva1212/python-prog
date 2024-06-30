
# The __init__() in python:

class book_shop:
    # Constructor
    def __init__(self,title):
        self.title = title
    # Sample method
    def book(self):
        print("The title of the book is",self.title)
b = book_shop('sandman')
b.book()
# The title of the book is sandman