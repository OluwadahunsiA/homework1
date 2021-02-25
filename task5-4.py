from functools import reduce

even = [integer for integer in range(100, 1000+1) if integer % 2 == 0]


def multiplication(value1, value2):
    return value1 * value2


print(reduce(multiplication, even))
