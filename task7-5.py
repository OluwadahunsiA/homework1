import json
with open('company.txt', 'r+') as file:
    company_dict = {}
    company_average = {}
    avg = []
    result = []
    for firm in file.readlines():
        new_list = []
        for val in firm.split(' ')[2:]:
            new_list.append(int(val.rstrip('.\n')))
        company_dict[firm.split(' ')[0]] = (new_list[0]-new_list[1])
        if (new_list[0]-new_list[1]) > 0:
            avg.append(new_list[0]-new_list[1])

    company_average['average_profit'] = round((sum(avg)/len(avg)), 2)
    result.append(company_dict)
    result.append(company_average)

print(f'\n{result}\n')

with open('company_result.json', 'w+') as company:
    json.dump(result, company)
