import random

class Product:
    def __init__(self, name, price = 10, weight = 20, flammability = 0.5, identifier = random.randint(1000000,9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        if (self.price / self.weight) < 0.5:
            print('Not so stealable...')
        elif (self.price / self.weight) >= 0.5:
            print('Kinda stealable.')
        else:
            return 'Very stealable!'

    def explode(self):
        if (self.flammability * self.weight) < 10:
            print('...fizzle.')
        elif (self.flammability * self.weight) in range(10, 50):
            print('...boom!')
        else:
            "BABOOM!!"

class BoxingGlove(Product):
    def __init__(self, name, weight = 10, price = 10, flammability = 0.5, identifier = random.randint(1000000,9999999)):
        super().__init__(name = name, price = price, weight = weight, flammability = flammability, identifier=identifier)
        
    def explode(self):
        return "...it's a glove."
        
    def punch(self):
        if self.weight < 5:
            print('That tickles')
        elif self.weight in range(5,15):
            print('Hey that hurt!')
        else:
            return 'OUCH!'