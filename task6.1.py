import time


class TrafficLight():
    def __init__(self):
        self.__color = 'red'

    def running(self):
        print(self.__color)
        # Countdown
        for i in range(6, -1, -1):
            print(f'Waiting....:{i}', end='\r')
            time.sleep(1)
        # Next color
        self.__color = 'Yellow'
        print(f'\n{self.__color}')
        # Countdown
        for i in range(2, -1, -1):
            print(f'Waiting....:{i}', end='\r')
            time.sleep(1)
        # Next color
        self.__color = 'Green'
        print(f'\n{self.__color}')


x = TrafficLight()

x.running()
