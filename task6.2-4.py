from sys import argv
from itertools import cycle, count

script_name = argv

initial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
counter = 0
for value in cycle(initial):
    if counter > 20:
        break
    else:
        print(value)
        counter += 1
