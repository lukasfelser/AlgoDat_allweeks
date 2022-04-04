
def count_vowels(text):
    if not isinstance(text, str):
        return 42
    count = 0
    text = text.lower()
    vowels = "aeiou"
    for letter in text:
        if letter in vowels:
            count += 1
    return count


def hamming(text1, text2):
    if len(text1) != len(text2):
        return 0
    hamming_distance = 0
    for number in range(0, len(text1)):
        if text1[number] != text2[number]:
            hamming_distance += 1
    return hamming_distance


# aufgabe 3

class Vehicle:
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type


class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        return "Color: {0}, Fuel Type: {1}, Doors: {2}".format(self.color, self.fuel_type, self.doors)


class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return "Color: {0}, Fuel Type: {1}, Passengers: {2}".format(self.color, self.fuel_type, self.passengers)


# aufgabe 4

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return "{0}, {1}".format(self.name, self.author)


# aufgabe 5

class BookShelf:

    def __init__(self):
        self.books = []

    def add_book_list(self, new_books):
        for entry in new_books:
            if isinstance(entry, Book):
                self.books.append(entry)

    def books_by_author(self, author):
        names = []
        for entry in self.books:
            if entry.author == author:
                names.append(entry.name)
        return names

    def get_books(self):
        names = []
        for entry in self.books:
            names.append(entry.name)
        return names

    def clear_shelf(self):
        self.books.clear()
