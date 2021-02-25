def my_func(x, y):
    initial = 1
    if x > 0 and y < 0:
        for _ in range(-y):
            initial *= (1 / x)
    else:
        print('Check that the first argument is positive and the second is negative')
    print(f'{x} ^ ({y}) = {initial:.7f}')


# def my_func(x, y):
#     if x > 0 and y < 0:
#         print(f'{x} ^ ({y}) = {x ** (y):.7f}')
#     else:
#         print('Please enter the right values')


my_func(50, -3)
