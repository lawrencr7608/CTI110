# The program is to calculate number of pizzas (6 slices per pizza) you need to order for a group of students
# April 7th, 2022
# CTI-110 P1HW2 - Pizza Order
# Rashad Lawrence

Students = int(input('How many students do you want to order pizza for?'))

pizzaSlices = Students * 3

Pizzas = pizzaSlices / 6

print('-------Pizza Order-----------')
print('Number of Students :',Students)
print('Pizza Slices needed:',pizzaSlices)
print('Pizzas needed :',Pizzas)
print('-----------------------------')
