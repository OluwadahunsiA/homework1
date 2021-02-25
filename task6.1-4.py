from sys import argv
from itertools import cycle, count

script_name, x = argv

for n in count(int(x)):
    if n > 10:
        break
    else:
        print(n)
        n += n
