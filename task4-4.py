initial = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

final = [value for value in initial if initial.count(value) == 1]

print(final)
