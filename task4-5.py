word_dict = {'one': 'Oдин', 'two': 'Два', 'three': 'Три', 'four': 'Четыре'}
translated_words = []

with open('numbers.txt', 'r+') as numbers:
    lines = numbers.readlines()
    for line in lines:
        splitted = line.split(' ')
        splitted[0] = word_dict[splitted[0].lower()]
        translated_words.append(splitted)

with open('new_numbers.txt', 'a') as new_num:
    for each in translated_words:
        new_num.write(' '.join(each))
