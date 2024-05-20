def z1():
    class Restaurant:
        def __init__(self, name, cuisine):
            self.name = name
            self.cuisine = cuisine
        def describe(self):
            print(f'Ресторан "{self.name}":  {self.cuisine} кухня')
        def open(self):
            print(f'"{self.name}" сейчас открыт')

    myRestaurant = Restaurant("Рай грузина", "Грузинская")
    myRestaurant.describe()
    myRestaurant.open()

def z2():
    class Restaurant:
        def __init__(self, name, cuisine):
            self.name = name
            self.cuisine = cuisine

        def describe(self):
            print(f'Ресторан "{self.name}":  {self.cuisine} кухня')

        def open(self):
            print(f'"{self.name}" сейчас открыт')
    Restaurant1 = Restaurant("Рай грузина", "Грузинская")
    Restaurant2 = Restaurant("Рай азиата", "Азиатская")
    Restaurant3 = Restaurant("Рай американца", "Фаста - фуд")
    Restaurant1.describe()
    Restaurant2.describe()
    Restaurant3.describe()


def z3():
    class Restaurant:
        def __init__(self, name, cuisine, rating):
            self.name = name
            self.cuisine = cuisine
            self.rating = rating
        def describe(self):
            print(f'Ресторан "{self.name}":  {self.cuisine} кухня')
        def open(self):
            print(f'"{self.name}" сейчас открыт')
        def newRating(self, new_rating):
            if new_rating > 0 and new_rating <= 10:
                self.rating = new_rating
            print(f'Рейтинг: {self.rating} очков')
    Restaurant1 = Restaurant("Рай грузина", "Грузинская", 5)
    Restaurant2 = Restaurant("Рай азиата", "Азиатская", 3)
    Restaurant3 = Restaurant("Рай американца", "Фаста - фуд", 0)
    Restaurant1.describe()
    Restaurant1.newRating(0)
    Restaurant2.describe()
    Restaurant2.newRating(0)
    Restaurant3.describe()
    Restaurant3.newRating(0)
z3()