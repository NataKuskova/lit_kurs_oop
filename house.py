class Properties:
    length = None
    width = None
    height = None
    coordinate = {}

    def __init__(self, **kwargs):
        self.length = kwargs['length']
        self.width = kwargs['width']
        self.height = kwargs['height']
        self.coordinate = kwargs['coordinate']


class Furniture(Properties):
    # мебель
    material = None
    weight = None

    def __init__(self, **kwargs):
        self.material = kwargs['material']
        self.weight = kwargs['weight']
        super().__init__(**kwargs)


class Appliance(Properties):
    # приборы
    energy_consumption = None
    opening_hours = None  # часы работы
    weight = None

    def __init__(self, **kwargs):
        self.energy_consumption = kwargs['energy_consumption']
        self.opening_hours = kwargs['opening_hours']
        self.weight = kwargs['weight']
        super().__init__(**kwargs)

    def energy_consumption_one(self):
        day = self.energy_consumption * self.opening_hours
        day /= 1000
        month = day * 30
        return month


class Table(Furniture):
    # стол
    pass


class Chair(Furniture):
    # стул
    pass


class Cupboard(Furniture):
    # шкаф
    pass


class Sofa(Furniture):
    # диван
    pass


class TV(Furniture):
    # телевизор
    pass


class Bed(Furniture):
    # кровать
    pass


class Refrigerator(Appliance):
    # холодильник
    pass


class Oven(Appliance):
    # духовка
    pass


class Sink(Furniture):
    # раковина
    pass


class Heater(Appliance):
    # обогреватель
    pass


class Conditioner(Appliance):
    # кондиционер
    pass


class WinDoor(Furniture):
    # окна, двери
    kind = None

    def __init__(self, **kwargs):
        self.kind = kwargs['kind']
        super().__init__(**kwargs)


class Room(Properties):
    furniture = None
    win_door = []

    def __init__(self, **kwargs):
        self.furniture = kwargs['furniture']
        self.win_door = kwargs['win_door']
        super().__init__(**kwargs)

    def volume(self):
        return self.length * self.width * self.height

    def weight(self):
        sum_ = sum([furniture.weight for furniture in self.furniture])
        sum_ += sum([win_door.weight for win_door in self.win_door])
        return sum_

    def energy_consumption_month(self):
        energy = 0
        for furniture in self.furniture:
            if isinstance(furniture, Appliance):
                energy += furniture.energy_consumption_one()
        return energy


class Kitchen(Room):
    # кухня
    pass


class Bedroom(Room):
    # спальня
    pass


class Hall(Room):
    # зал
    pass


class Corridor(Room):
    # коридор
    pass


class House(Properties):
    rooms = None

    def __init__(self, **kwargs):
        self.rooms = kwargs['rooms']
        super().__init__(**kwargs)

    def volume_house(self):
        return sum([room.volume() for room in self.rooms])

    def weight_house(self):
        return sum([room.weight() for room in self.rooms])

    def energy_consumption(self):
        return sum([room.energy_consumption_month() for room in self.rooms])


if __name__ == "__main__":
    house = House(
        rooms=[
            Kitchen(
                furniture=[
                    Refrigerator(
                        energy_consumption=250,
                        opening_hours=8,
                        length=0.6,
                        width=0.5,
                        height=1.5,
                        weight=70,
                        coordinate={
                            'left_bottom': (0, 1),
                            'right_top': (0.6, 1.5)
                        }
                    ),
                    Oven(
                        energy_consumption=3000,
                        opening_hours=4,
                        length=0.5,
                        width=0.5,
                        height=0.5,
                        weight=33,
                        coordinate={
                            'left_bottom': (2, 0),
                            'right_top': (2.5, 0.5)
                        }
                    )
                ],
                length=4,
                width=3,
                height=3,
                win_door=[
                    WinDoor(
                        kind='door',
                        length=1,
                        width=0.1,
                        height=2,
                        weight=50,
                        material='wood',
                        coordinate={
                            'left_bottom': (4, 1),
                            'right_top': (4, 2)
                        }
                    ),
                    WinDoor(
                        kind='window',
                        length=1.5,
                        width=0.2,
                        height=1.5,
                        weight=45,
                        material='plastic',
                        coordinate={
                            'left_bottom': (0, 1),
                            'right_top': (0, 2.5)
                        }
                    )
                ],
                coordinate={
                    'left_bottom': (0, 0),
                    'right_top': (4, 3)
                }
            ),
            Corridor(
                furniture='',
                length=7,
                width=2,
                height=3,
                win_door=[
                    WinDoor(
                        kind='door',
                        length=1,
                        width=0.1,
                        height=2,
                        weight=50,
                        material='wood',
                        coordinate={
                            'left_bottom': (4.5, 0),
                            'right_top': (5.5, 0)
                        }
                    )
                ],
                coordinate={
                    'left_bottom': (4, 0),
                    'right_top': (6, 7)
                }
            )
        ],
        length=10,
        width=7,
        height=3,
        coordinate={
            'left_bottom': (0, 0),
            'right_top': (10, 7)
        }
    )
    weight = house.weight_house()
    print("The weight of house = " + str(weight) + " kg")
    volume = house.volume_house()
    print("The volume of house = " + str(volume) + " m^3")
    energy = house.energy_consumption()
    print("Energy consumption per month = " + str(energy) + " kW/h")
