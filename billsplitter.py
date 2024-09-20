from random import choice
people_wanna_join = int(input('Enter the number of friends joining (including you):'))
if people_wanna_join <= 0:
    print('No one is joining for the party')

else:
    names = []
    for i in range(people_wanna_join):
        names.append(input())
    total_bill_value = int(input('Enter the total bill value: '))
    

    lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_perspn = choice(names)
    if lucky_feature == 'Yes':
        print(f'{lucky_perspn} is the lucky one!')
        split_value = round((total_bill_value / (people_wanna_join - 1)), 2)
        output = {name: split_value for name in names if name != lucky_perspn}
        output[lucky_perspn] = 0
        print(output)
    else:
        split_value = round((total_bill_value / people_wanna_join), 2)
        print('No one is going to be lucky', {name: split_value for name in names}, sep='\n')