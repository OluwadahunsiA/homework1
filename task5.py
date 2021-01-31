revenue = int(input('Ваши выручки: '))

cost = int(input('Ваши издержки: '))

if revenue > cost:
    print('Финансовый результат: прибыль')

    print(f'рентабельность выручки: {(revenue-cost)/revenue}')

    workers = int(input("Численность сотрудников фирмы: "))

    profitperhead = (revenue - cost) / workers

    print(f'Прибыль фирмы в расчете на одного сотрудника: {profitperhead}')

else:

    print('Финансовый результат: убыток')
