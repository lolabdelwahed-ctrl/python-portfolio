# 2025-03-02
# Purpose: This project was created in order to refine my use of functions
# Break Even calculation
import math

def break_even(fixed_cost, selling_price, unit_cost):
    if selling_price <= unit_cost:
        return 'your unit cost can not be higher or equal to the selling price in this calculation '
        
    BEP = fixed_cost/(selling_price-unit_cost)
    return math.ceil(BEP)

user_fixed_cost = float(input('What is the total fixed cost? (ONLY numbers) '))
user_selling_price = float(input('What is the selling price of each unit '))
user_unit_cost = float(input('What is the cost per unit '))

units_required = break_even(user_fixed_cost, user_selling_price, user_unit_cost)

# Note: Logic below was NOT of my own creation but was created with the help of a friend
if type(units_required) == str:
    print (units_required)
else:
    print (f'You need {units_required} in order to break even')


