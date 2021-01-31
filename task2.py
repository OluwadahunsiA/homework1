timer = int(input('Enter time in seconds: '))

hour = timer // 3600
remainder = timer % 3600
minute = remainder // 60
remainder = remainder % 60
second = remainder

print(f'{hour:02d}:{minute:02d}:{second:02d}')
