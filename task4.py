
number = input('Enter your number: ')

length = len(number)  # this takes the length of the number entered

lastnumber = 0  # this value might change after iteration

while length > -1:

    divide1 = int(number)//(10 ** (length-1))  # get the first digit

    remainder = int(number) % (10 ** (length-1))  # get the remainder

    number = remainder  # set number = remainder for next iteration

    length -= 1        # reduce the length of the number

    if divide1 > lastnumber:

        lastnumber = divide1

    else:

        lastnumber = lastnumber

print(lastnumber)
