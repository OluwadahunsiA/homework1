class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'The car has moved'

    def stop(self):
        return 'The car has stopped'

    def turn(self, direction):
        return f'The car has turned {direction}'

    def show_speed(self, speed):
        if speed < 60:
            print('Within speed limit')
        else:
            print('Overspeeding')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self, speed):
        if speed > 60:
            print('Overspeeding!!!')
        else:
            print('Within speed limit')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)
        if speed < 100:
            print(f'Your speed is {self.speed} km/h, you can speed more')
        else:
            print('Keep going')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):

        super().__init__(speed, color, name, is_police=False)

    def show_speed(self, speed):
        if speed > 60:
            print('Overspeeding!!!')
        else:
            print('Within speed limit')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)
        if is_police == True:

            print(f'Police is here')


police = PoliceCar(70, 'Red', 'Alfredo', True)
worker = WorkCar(70, 'Red', 'Alfredo', True)
athlete = SportCar(70, 'Red', 'Alfredo')
worker.show_speed(100)
resident = TownCar(70, 'Red', 'Alfredo')
resident.show_speed(80)
