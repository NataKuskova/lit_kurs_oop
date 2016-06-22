class VolumeMixin(object):

    def volume(self):
        pass


class WeightMixin(object):

    def weight(self):
        pass


class Furniture(WeightMixin, object):
    # мебель
    material = None
    width = None
    height = None
    x = None
    y = None

    def __init__(self, material, width, height):
        self.material = material
        self.width = width
        self.height = height


class Appliance(Furniture, object):
    # приборы
    pass


class Table(Furniture):
    # стол
    pass


class Chair(Furniture):
    # стул
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


class Room(VolumeMixin, object):
    furniture = None
    length = None
    width = None
    height = None
    x = None
    y = None
    win_door = []

    def __init__(self, furniture, length, width, height, win_door):
        self.furniture = furniture
        self.length = length
        self.width = width
        self.height = height
        self.win_door = win_door

    def volume(self):
        return self.length * self.width * self.height


class Kitchen(Room):
    # кухня
    pass


class Bedroom(Room):
    # спальня
    pass


class Hall(Room):
    # зал
    pass


class House(WeightMixin, VolumeMixin, object):
    rooms = None

    def __init__(self, rooms):
        self.rooms = rooms

    def volume(self):
        return sum([room.volume for room in self.rooms])


if __name__ == "__main__":
    pass
