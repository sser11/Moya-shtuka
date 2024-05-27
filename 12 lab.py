from tkinter import *
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
        def type(self, morozh):
            if morozh == 'мороженое на палочке':
                myRestaurant.location()
                print('Вы выбрали мороженое на палочке')
            elif morozh == 'мягкое мороженое':
                myRestaurant.location()
                print('Вы выбрали мягкое мороженое')
            else:
                myRestaurant.location()
                print('Вы выбрали другое мороженое')
    myRestaurant = IceCreamStand("Рай мороженщика", "Холодная", "малиновое, шоколадное, клубничное", "Невский проспкт, дом 9", "09:00 - 23:00")
    a = input('Какое мороженое вы хотите заказать?')
    myRestaurant.type(a)
    myRestaurant.plus('ананасовое')
    myRestaurant.minus('шоколадное')
    myRestaurant.proverka('шоколадное')
    myRestaurant.sorts()

def z3():
    import tkinter as tk

class IceCreamStand:
    def __init__(self, name, location, hours, flavors):
        self.name = name
        self.location = location
        self.hours = hours
        self.flavors = flavors

    # ... (остальной код из задания 12.2)

    def create_window(self):
        # Создание главного окна
        self.window = tk.Tk()
        self.window.title(self.name)

        # Создание виджетов для вывода информации
        self.location_label = tk.Label(self.window, text=f"Локация: {self.location}")
        self.hours_label = tk.Label(self.window, text=f"Время работы: {self.hours}")
        self.flavors_label = tk.Label(self.window, text="Доступные сорта мороженого:")

        # Создание виджетов для добавления и удаления вкусов
        self.add_flavor_entry = tk.Entry(self.window)
        self.add_flavor_button = tk.Button(self.window, text="Добавить сорт", command=self.add_flavor)
        self.remove_flavor_entry = tk.Entry(self.window)
        self.remove_flavor_button = tk.Button(self.window, text="Удалить сорт", command=self.remove_flavor)

        # Создание виджетов для проверки наличия вкуса
        self.check_flavor_entry = tk.Entry(self.window)
        self.check_flavor_button = tk.Button(self.window, text="Проверить наличие сорта", command=self.check_flavor)

        # Создание виджетов для разных типов мороженого
        self.add_popsicle_entry = tk.Entry(self.window)
        self.add_popsicle_button = tk.Button(self.window, text="Добавить на палочке", command=self.add_popsicle)
        self.remove_popsicle_entry = tk.Entry(self.window)
        self.remove_popsicle_button = tk.Button(self.window, text="Удалить на палочке", command=self.remove_popsicle)

        self.add_soft_serve_entry = tk.Entry(self.window)
        self.add_soft_serve_button = tk.Button(self.window, text="Добавить мягкое", command=self.add_soft_serve)
        self.remove_soft_serve_entry = tk.Entry(self.window)
        self.remove_soft_serve_button = tk.Button(self.window, text="Удалить мягкое", command=self.remove_soft_serve)

        # Размещение виджетов в главном окне
        self.location_label.pack()
        self.hours_label.pack()
        self.flavors_label.pack()

        self.add_flavor_entry.pack()
        self.add_flavor_button.pack()
        self.remove_flavor_entry.pack()
        self.remove_flavor_button.pack()

        self.check_flavor_entry.pack()
        self.check_flavor_button.pack()

        self.add_popsicle_entry.pack()
        self.add_popsicle_button.pack()
        self.remove_popsicle_entry.pack()
        self.remove_popsicle_button.pack()

        self.add_soft_serve_entry.pack()
        self.add_soft_serve_button.pack()
        self.remove_soft_serve_entry.pack()
        self.remove_soft_serve_button.pack()

        # Запуск главного цикла окна
        self.window.mainloop()

# Создание экземпляра класса IceCreamStand
my_ice_cream_stand = IceCreamStand("Рай мороженщика", "ул. Ленина, 15", "10:00-22:00", ["Малиновое", "Шоколадное", "Клубничное"])

# Создание графического интерфейса
my_ice_cream_stand.create_window()
