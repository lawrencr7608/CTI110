#Calculate subtotal, sales tax, and the overall total of five purchased items.
#April 4th, 2022
#CTI-110 P2HW1 - Total Purchases
#Rashad Lawrence
#

#//Get 5 item inputs
item1 = float(input('Enter the price of item #1:'))
item2 = float(input('Enter the price of item #2:'))
item3 = float(input('Enter the price of item #3:'))
item4 = float(input('Enter the price of item #4:'))
item5 = float(input('Enter the price of item #5:'))

#//Calculate subtotal, sales tax, and overall total
subtotal = item1 + item2 + item3 + item4 + item5
sales_tax = subtotal*.07
Total = subtotal + sales_tax

#//output results
print('-------Results--------')
print(f'Subtotal: {subtotal:.2f}')
print(f'Sales Tax: {sales_tax:.2f}')
print(f'(Total: {Total:.2f}')
print('---------------------')
