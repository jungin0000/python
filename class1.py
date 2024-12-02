class book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.prcie = price

    def display(self):
         print("title  =", self.title)
         print("author  =", self.author)
         print("price  =", self.price)

    def __eq__(self, other):
        if isinstance(other, book):
            if self.price==other.price:
                return True
            else:
                return False