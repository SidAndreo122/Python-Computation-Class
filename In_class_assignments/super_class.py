# some_inheritance.py
class Engine:
  def start(self):
      return
  def stop(self):
      pass
class ElectricEngine(Engine):  # Is-A Engine
  pass
class V8Engine(Engine):  # Is-A Engine
  pass

class Headlights:
  def lights_on(self):
    print('Lights are on')

  def lights_off(self):
    print('lights are off')

class Car:
    engine_cls = Engine
    headlights_cls = Headlights
    def __init__(self):
        self.engine = self.engine_cls()  # Has-A Engine
        self.headlight = self.headlights_cls()
    def start(self):
        print(
            'Starting engine {0} for car {1}... Wroom, wroom!'
            .format(
                self.engine.__class__.__name__,
                self.__class__.__name__)
        )
        self.engine.start()
        self.headlight.lights_on()
    def stop(self):
        self.engine.stop()
        self.headlight.lights_off()
class RaceCar(Car):  # Is-A Car
    engine_cls = V8Engine
class CityCar(Car):  # Is-A Car
    engine_cls = ElectricEngine
class F1Car(RaceCar):  # Is-A RaceCar and also Is-A Car
    pass  # engine_cls same as parent
car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()
cars = [car, racecar, citycar, f1car]
for car in cars:
    car.start()


