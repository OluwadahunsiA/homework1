def Details(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}', end='  ')


Details(name='Oluwadahunsi', surname='Alawode', Date_of_Birth='15.05.2020', city_of_residence='Moscow')
