initial = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

final = [value for value in initial if value >
         initial[initial.index(value)-1] and initial.index(value)-1 > -1]
print(final)
