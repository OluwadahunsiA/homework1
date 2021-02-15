
proceed = True

while proceed:
    value = input('Enter text to append. Press ENTER to escape: ')
    with open('data.txt', 'a+') as data:
        data.write(value + '\n')
    if value == '':
        proceed == False
        break
    else:
        continue
