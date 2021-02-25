
with open('workers.txt', 'r+') as worker:
    detail = worker.readlines()

new_list = []
for worker in detail:
    income_list = worker.split(' ')
    new_list.append(int(income_list[1]))
    if int(income_list[1]) < 20000:
        print(f'{income_list[0]} has income less than 20 000')


print(f'Total average: {sum(new_list)/len(new_list):.2f}')
