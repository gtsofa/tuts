class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model
        #note - identy code is a MUST
mustang = Car('Porsh', 'Mustang')
print(mustang.wheels)
print(Car.wheels)
