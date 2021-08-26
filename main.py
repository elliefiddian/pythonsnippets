meal_price = float(input('How much did the meal cost? '))
discount_applied = input('Do you have a discount code? y/n ')

discount_applicable = discount_applied == 'y'

if discount_applicable:
    meal_price = meal_price * 0.9
    print('Discount applied')
else:
    print('No discount')

print('Total cost: {}'.format(meal_price))