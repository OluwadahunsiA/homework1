class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self, unit_mass, thickness=1):
        return f'{self._length}m * {self._width}m * {unit_mass}Kg * {thickness}cm = {int(self._length * self._width * unit_mass * (thickness/1000))} T'


way = Road(20, 5000)
print(way.mass_calc(25, 5))
