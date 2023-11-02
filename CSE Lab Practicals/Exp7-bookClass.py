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
        return super().__str__() + f", {self.subgenre}"
    

class Fiction(Book):
    def __init__(self, name, author, price, genre, subgenre):
        super().__init__(name, author, price, genre)
        self.subgenre = subgenre
    def __str__(self):
        return super().__str__() + f", {self.subgenre}"
    
x = Book("The Alchemist", "Paulo Coelho", 350, "Fiction")
y = Detective("The Hound of Baskervilles", "Arthur Conan Doyle", 250, "Detective", "Sherlock Holmes")
z = Fiction("The Alchemist", "Paulo Coelho", 350, "Fiction", "Adventure")
print(x)
print(y)    
print(z)    
