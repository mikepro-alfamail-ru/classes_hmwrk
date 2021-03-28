class animal():
    def __init__(self, name='', weight=0):
        self.name = name
        self.weight = weight
        self.life = 100
        self.food = 0

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
        return self

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
    duck1.feed(150)
    next(duck1)
    print(duck1.type, duck1.name, duck1.weight)

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