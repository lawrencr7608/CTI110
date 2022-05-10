# CTI-110
# P4HW2 - Pizza Order
# Rashad Lawrence
# 5-9-2022
#

import math
cond = 'Y'

if cond == 'Y' or cond == 'y':
    import math
    students = float(input('How many students do you want to order for?'))
    pperp = float(input('How many people per pizza(1.5, 2, or 3)?'))
    pizza = 0
    if pperp != 1.5 or 2 or 3:
        print('INVALID ENTRY!!!!')
        print('Should have entered 1.5, 2, or 3')
        print('Run program again')
    if pperp == 1.5 or 2 or 3:
        if pperp == 1.5:
            pizza = (students/pperp)
            pizza = math.ceil(pizza)
            cost = (pizza * 5) 
        elif pperp == 2:
            pizza = (students/pperp)
            pizza = math.ceil(pizza)
            cost = pizza * 5
        elif pperp == 3:
            pizza = (students/pperp)
            pizza = math.ceil(pizza)
            cost = pizza * 5
    print('-----Pizza Order------')
    print('Number of Students :', students)
    print('Pizzas needed :', pizza)
    print('price:$', cost)
    print('----------------------')
    cond = input('Would you like to run the program again? (Type Y for yes)')


