class EngineMixin:
    def engine_on(self):
        print("engine on")

class WheelMixin:
    def first_spin(self):
        print("spin...")

    def second_spin(self):
        print("spin...")


class Car(EngineMixin, WheelMixin):
    def __init__(self, model):
        self._model = model


c = Car("aaaa")
c.engine_on()
c.first_spin()
