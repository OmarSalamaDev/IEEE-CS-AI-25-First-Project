
# todo make class book -> Sohaila

class Book:


    def __init__(self, title, author, price, description, isbn, category, publisher):
        self.title = title
        self.author = author
        self.price = price
        self.description = description
        self.isbn = isbn
        self.category = category
        self.publisher = publisher


    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}\nDescription: {self.description}\nISBN: {self.isbn}\nCategory: {self.category}\nPublisher: {self.publisher}"
