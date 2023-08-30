class Book:
    def __init__(self, name, author, price, genre):
        self.name = name
        self.author = author
        self.price = price
        self.genre = genre
    def __str__(self):
        return f"{self.name} by {self.author} ({self.price}) \n{self.genre}"

class Detective(Book):
    def __init__(self, name, author, price, genre, subgenre):
        super().__init__(name, author, price, genre)
        self.subgenre = subgenre
    def __str__(self):
        return super().__str__() + f"{self.subgenre}"
    