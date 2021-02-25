with open('page.txt', 'r+') as page:
    read = page.readlines()

linecounter = 0
textcounter = 0
for line in read:
    linecounter += 1
    for text in line.strip():
        textcounter += 1
    print(f'Line {linecounter} has {textcounter} word(s)\n')
    textcounter = 0

print(f'There are {linecounter} lines')
