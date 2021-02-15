free_dict = {}

with open('courses.txt', 'r+') as file:

    for course in file.readlines():

        new_string = ''.join((i if i in '01234567890' else ' ')
                             for i in ''.join(course.split(' ')[1:]))

        new_list = []
        for val in new_string.strip().split(' '):
            if val.isdigit():
                new_list.append(int(val))
                free_dict[course.split(' ')[0].replace(
                    ':', '')] = sum(new_list)
print(free_dict)
