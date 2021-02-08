def Divider(a, b):
    a = float(input('Enter the numerator: '))
    b = float(input('Enter the denominator: '))
    if b == 0:
        print('This operation is impossible.')
        return
    else:
        print(f'The result of your division is: {a/b:.2f}')
        return


Divider(5, 2)
