class animal():
    def __init__(self, name='', weight=0):
        self.name = name
        self.weight = weight
        self.life = 100
        self.food = 0
        self.lifecycle = 0

    def feed(self, f_count):
        self.food += f_count

    def __iter__(self):
        return self

    def __next__(self):
        self.life -= (100 - self.food) / 5
        self.weight *= 1 - (100 - self.food) / 500
        if self.life < 0:
            self.life = 0
        self.food = 0
        self.lifecycle += 1
        return self

class wool():
    def __init__(self):
        self.woolleft = 100

    def get_wool(self, amount):
        if amount > self.woolleft:
            amount = self.woolleft
        self.woolleft -= amount
        return amount

    def __next__(self):
        if self.food >= 100:
            self.woolleft = 100
        super(wool, self).__next__()


class milk():
    def __init__(self):
        self.milkleft = 100

    def get_milk(self, amount):
        self.milkleft -= amount
        return self.milkleft

class eggs():
    def __init__(self):
        self.eggsleft = 100

    def get_wool(self, amount):
        self.eggsleft -= amount
        return self.eggsleft

class goose(eggs, animal):
    def __init__(self, *args):
        animal.__init__(self, *args[:2])
        self.type = 'Гусь'

class cow(milk, animal):
    def __init__(self, *args):
        animal.__init__(self, *args)
        self.type = 'Корова'


class sheep(wool, animal):
    def __init__(self, *args):
        animal.__init__(self, *args[:2])
        wool.__init__(self)
        self.type = 'Овца'


class hen(eggs, animal):
    def __init__(self, *args):
        animal.__init__(self, *args[:2])
        self.type = 'Курица'


class goat(milk, animal):
    def __init__(self, *args):
        animal.__init__(self, *args[:2])
        self.type = 'Коза'


class duck(eggs, animal):
    def __init__(self, *args):
        animal.__init__(self, *args[:2])
        self.type = 'Утка'

def printstatus(animals):
    print('Тип  ', 'Имя    ', 'Здоровье', 'Вес', sep='\t\t\t')
    for animal in animals:
        print(animal.type, animal.name, animal.life, animal.weight, sep='\t\t\t')

def main():
    animals = [
        goose('Серый', 10),
        goose('Белый', 12),
        cow('Манька', 550),
        sheep('Барашек', 200),
        sheep('Кудрявый', 190),
        hen('Ко-Ко', 5),
        hen('Кукаруку', 4),
        goat('Рога', 90),
        goat('Копыта', 60),
        duck('Кряква', 4)
    ]
    printstatus(animals)
    animals[3].get_wool(50)
    for anima in animals:
        next(anima)
    printstatus(animals)

    for anima in animals:
        next(anima)
    printstatus(animals)

#    print(animals[3].lifecycle, animals[3].life, animals[3].woolleft)

def cow_ascii():
    print('''
           .        .
           \'.____.'/
          __'-.  .-'__                         .--.
          '_i:'oo':i_'---...____...----i"""-.-'.-"\\
            /._  _.\       :       /   '._   ;/    ;'-._
           (  o  o  )       '-.__.'       '. '.     '-."
            '-.__.-' _.--.                 '-.:
             : '-'  /     ;   _..--,  /       ;
             :      '-._.-'  ;     ; :       :
              :  `      .'    '-._.' :      /
               \  :    /    ____....--\    :
                '._\  :"""""    '.     !.   :
                 : |: :           'www'| \ '|
                 | || |              : |  | :
                 | || |             .' !  | |
                .' !| |            /__I   | |
               /__I.' !                  .' !
                  /__I                  /__I  
    ''')

if __name__ == '__main__':
    cow_ascii()
    main()