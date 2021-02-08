def int_func(*args):
    for vals in args:
        print(vals.title())


# OR

# def int_func(*args):
#     for vals in args:
#         if len(vals) == 1:
#             print(vals.capitalize())
#         elif len(vals) > 1:
#             print(vals.title())
#         else:
#             print('Enter the right thing')


int_func('he is a nice boy and you really have to meet him',
         'you are nice', 'he', 'they are your friend')
