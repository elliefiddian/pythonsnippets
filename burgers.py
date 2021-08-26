price = input('How much is the burger? ')
is_affordable = float(price) <= 10.00
print('The resturant is affordable: {}'.format(is_affordable))




price = input('How much is the burger? ')
veggie = input('Is there a veggie option? (y/n) ')

is_affordable = float(price) <= 10.00
has_veggie = veggie == 'y'

is_good_choice = is_affordable and has_veggie
print('Restaurant meets criteria: {}'.format(is_good_choice))