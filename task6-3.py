def int_func(word):
    words = 'abcdefghijklmnopqrstuvwxyz'
    empty = []
    for letter in word.split():
        if not set(letter).difference(words):
            empty.append(letter.title())
        else:
            continue
    print(' '.join(empty))


int_func('hello p1 you1 are good')

# for vals in args:
#     print(vals.title())

# OR

# def int_func(*args):
#     for vals in args:
#         if len(vals) == 1:
#             print(vals.capitalize())
#         elif len(vals) > 1:
#             print(vals.title())
#         else:
#             print('Enter the right thing')
