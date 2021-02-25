class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_integer(cls, date):
        new = date.split('-')
        return(f'Day: {int(new[0])}, Month: {int(new[1])}, Year: {int(new[2])}')

    @staticmethod
    def validator(date):
        new = date.split('-')
        day = int(new[0])
        month = int(new[1])
        year = int(new[2])

        if int(day) > 0 and int(day) < 32:
            print('Valid day')
        else:
            print('Not a valid day')
        if int(month) > 0 and int(month) >= 1 and int(month) <= 12:
            print('Valid month')
        else:
            print('Not a valid month')
        if len(new[2]) == 4 and year <= 2021 and year >= 0:
            print('Valid year')
        else:
            print('Not a valid year')

    def __str__(self):
        return f'Today\'s date is: {self.date} \n{Date.date_to_integer(self.date)}'


today = Date('02-02-2021')
Date.validator('10-12-2019')
print(Date.date_to_integer('02-02-2020'))
Date.validator('20-50-2020')


print(today)
