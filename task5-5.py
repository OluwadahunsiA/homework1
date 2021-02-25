with open('enter_number.txt', 'w+') as file:
    nums = input('Enter comma separated numbers: ')
    file.write(nums)
    entered = file.read()

sum = 0
with open('enter_number.txt', 'r') as name:
    for line in name.readlines():
        for val in line.split(','):
            sum += int(val)
print('*******************')
print(f'The sum of the entered value is: {sum}')
print('*******************')
