def z1():
    class Restaurant:
        def __init__(self, name, cuisine):
            self.name = name
            self.cuisine = cuisine

        def describe(self):
            print(f'Ресторан "{self.name}":  {self.cuisine} кухня')

        def open(self):
            print(f'"{self.name}" сейчас открыт')
    class IceCreamStand(Restaurant):
        def __init__(self, name, cuisine, flavors):
            super().__init__(name, cuisine)
            self.flavors = flavors

        def describe(self):
            super().describe()

        def open(self):
            super().open()

        def sorts(self):
            print(f'Доступные сорты мороженого: {self.flavors}')

    myRestaurant = IceCreamStand("Рай мороженщика", "Холодная", "Малиновое, шоколадное, клубничное")
    myRestaurant.describe()
    myRestaurant.open()
    myRestaurant.sorts()

def z2():
    class Restaurant:
        def __init__(self, name, cuisine):
            self.name = name
            self.cuisine = cuisine

        def describe(self):
            print(f'Ресторан "{self.name}":  {self.cuisine} кухня')

        def open(self):
            print(f'"{self.name}" сейчас открыт')

    class IceCreamStand(Restaurant):
        def __init__(self, name, cuisine, flavors, place, time):
            super().__init__(name, cuisine)
            self.flavors = flavors
            self.place = place
            self.time = time

        def sorts(self):
            print(f'Доступные сорты мороженого: {self.flavors}')
        def location(self):
            print(f'"{self.name}" находится по адресу: {self.place} и работает по графику {self.time}.')

        def plus(self, new_flavors):
            b = self.flavors.split(', ')
            n = 0
            for i in range(len(b)):
                if new_flavors != b[i]:
                    n += 1
                else:
                    n = 0
                    break
            if n != 0:
                self.flavors += f', {new_flavors}'
        def minus(self, del_flavors):
            b = self.flavors.split(', ')
            a = ''
            for i in range(len(b)):
                if del_flavors == b[i]:
                    continue
                else:
                    a += f', {b[i]}'
            self.flavors = a[2:]
        def proverka(self, nal_flavors):
            b = self.flavors.split(', ')
            n = 0
            for i in range(len(b)):
                if nal_flavors == b[i]:
                    n += 1
            if n == 1:
                print(f'Мороженое со вкусом "{nal_flavors}" в наличии.')
            else:
                print(f'Мороженого со вкусом "{nal_flavors}" нет в наличии.')
    myRestaurant = IceCreamStand("Рай мороженщика", "Холодная", "малиновое, шоколадное, клубничное", "Невский проспкт, дом 9", "09:00 - 23:00")
    myRestaurant.location()
    myRestaurant.plus('ананасовое')
    myRestaurant.minus('шоколадное')
    myRestaurant.proverka('шоколадное')
    myRestaurant.sorts()
z2()