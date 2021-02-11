from sys import argv

script_name, hourly_rate, hourly_income, bonus = argv


def Salary(hourly_rate, hourly_income, bonus):
    print(f'Script name: {script_name}')
    print(f'Hourly rate: {hourly_rate}')
    print(f'Hourly income: {hourly_income}')
    print(f'Bonus: {bonus}')
    print(f'\n')
    print(
        f'Total salary : {(int(hourly_rate) * int(hourly_income)) + int(bonus)}')


Salary(hourly_rate, hourly_income, bonus)
