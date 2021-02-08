def my_func():
    total = 0
    check = True
    while check:
        number = input('Enter numbers separated with space: ')
        lst = number.split(' ')
        for num in lst:
            if num.isdigit():
                total += int(num)
            else:
                check = False
                print(f'End! You have entered a special symbol "{lst[-1]}"')
                break
        print(f'current sum {total}')
        continue

    print(f'final sum {total}')


my_func()
