class animal():
    def __init__(self, name='', weight=0):
        self.name = name
        self.weight = weight

    def feed(self, f_count):
        self.weight += f_count

class wool():
    pass

class milk():
    pass

class eggs():
    pass

class goose(eggs, animal):
    def __init__(self, *args):
        animal.__init__(self, *args[:1])
        self.type = 'Гусь'

class cow(milk, animal):
    def __init__(self, *args):
        animal.__init__(self, *args)
        self.type = 'Корова'


class sheep(wool, animal):
    def __init__(self, *args):
        animal.__init__(self, *args)
        self.type = 'Овца'


class hen(eggs, animal):
    def __init__(self, *args):
        animal.__init__(self, *args)
        self.type = 'Курица'


class goat(milk, animal):
    def __init__(self, *args):
        animal.__init__(self, *args)
        self.type = 'Коза'


class duck(eggs, animal):
    def __init__(self, *args):
        animal.__init__(self, *args[:2])
        self.type = 'Утка'

def main():
    duck1 = duck('Кряква', 3)
    print(duck1.type, duck1.name, duck1.weight)
    duck1.feed(0.5)
    print(duck1.type, duck1.name, duck1.weight)

if __name__ == '__main__':
    main()