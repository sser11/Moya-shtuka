def z1():
    class IceCreamStand:
        def __init__(self, name, cuisine, flavors):
            self.name = name
            self.cuisine = cuisine
            self.flavors = flavors
        def describe(self):
            print(f'Ресторан "{self.name}":  {self.cuisine} кухня')
        def open(self):
            print(f'"{self.name}" сейчас открыт')
        def sorts(self):
            print(f'Доступные сорты мороженого: {self.flavors}')

    myRestaurant = IceCreamStand("Рай мороженщика", "Холодная", "Малиновое, шоколадное, клубничное")
    myRestaurant.describe()
    myRestaurant.open()
    myRestaurant.sorts()

def z2():
    class IceCreamStand:
        def __init__(self, name, cuisine, flavors):
            self.name = name
            self.cuisine = cuisine
            self.flavors = flavors
        def describe(self):
            print(f'Ресторан "{self.name}":  {self.cuisine} кухня')
        def open(self):
            print(f'"{self.name}" сейчас открыт')
        def sorts(self):
            print(f'Доступные сорты мороженого: {self.flavors}')

    myRestaurant = IceCreamStand("Рай мороженщика", "Холодная", "Малиновое, шоколадное, клубничное")
    myRestaurant.describe()
    myRestaurant.open()
    myRestaurant.sorts()