import abc

class Veichle(abc.ABC):
    @abc.abstractmethod
    def turn_on(self):
        pass

    @abc.abstractmethod
    def turn_off(self):
        pass

    @abc.abstractmethod
    def turn_right(self):
        pass

    @abc.abstractmethod
    def turn_left(self):
        pass

    @abc.abstractmethod
    def forward(self):
        pass

    @abc.abstractmethod
    def backwards(self):
        pass


class Car(Veichle):
    def turn_on(self):
        print("car turn on")

    def turn_off(self):
        print("car turn off")

    def turn_right(self):
        print("car turn right")

    def turn_left(self):
        print("car turn left")

    def forward(self):
        print("car forward")
    
c = Car()

class Airplane:
    pass

a = Airplane()

a.turn_on()
