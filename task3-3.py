def my_func(a, b, c):
    lst = [a, b, c]
    lst.remove(min(lst))
    print(f'The sum of {lst[0]} and {lst[1]}: {sum(lst)}')


my_func(123, 55, 130)
