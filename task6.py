firstday = int(input('First day result: '))

targetvalue = int(input('Enter target value: '))

count = 1

while firstday <= targetvalue:

    if count == 1:

        print(f'{count}-й день: {firstday} ')

        count += 1

    else:

        firstday = firstday + (firstday * 0.1)

        print(f'{count}-й день: {firstday:.2f} ')

        count += 1
