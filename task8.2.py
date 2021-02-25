class MyZeroDivision(Exception):
    def __init__(self, entry):
        self.entry = entry


value = int(input('a: '))
value2 = int(input('b: '))
try:
    try:
        newValue = value/value2
    except ZeroDivisionError:
        raise MyZeroDivision('Numerator will be divided by 1')
except MyZeroDivision as z:
    print(z)
    print(f'Your corrected result: {value / 1}')
