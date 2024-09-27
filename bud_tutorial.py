# You are going to travel to a different country, but you have some heavy luggage to transport. There are different fees associated with different weights of luggage.

# If the weight is over 70 pounds, then there is a 100 dollar fee. If the weight is between 50 to 70 pounds (including exactly 50 and 70 pounds) the fee is 50 dollars, otherwise the fee is 0 dollars. Create an if, elif, else statement to calculate and store the fee into a variable called fee. Make sure not to use multiple if statements.

# FREE = 0
# LIGHT_LIMIT = 50
# HEAVY_LIMIT = 70

# LIGHT_FEE = 50
# HEAVY_FEE = 100

# my_luggage_weight = 40
# my_luggage_weight = 50
# my_luggage_weight = 71
# my_luggage_weight = -1
# my_luggage_weight = 1_000_000

# fee  = FREE

# # the next two lines are equivalent:
# # if 50 <= my_luggage_weight <= 70:
# if (LIGHT_LIMIT <= my_luggage_weight) and (my_luggage_weight <= HEAVY_LIMIT):
#     fee = LIGHT_FEE
# elif my_luggage_weight > HEAVY_LIMIT:
#     fee = HEAVY_FEE

# print(f"Your luggage weight is {my_luggage_weight}")
# print(f"The fee for your luggage is {fee}")


# my_weight_luggage = 50

# HEAVYWEIGHT_LIMIT = 70
# LIGHTWEIGHT_LIMIT = 50
# LIGHT_FEE = 50
# HEAVY_FEE = 100

# if my_weight_luggage >= HEAVYWEIGHT_LIMIT:
#     print("my luggage is heavier than the heavy weight limit")
# elif HEAVYWEIGHT_LIMIT == LIGHT_FEE:
#     print("Heavy weight limit would be equal the light fee ")
# elif my_weight_luggage >= LIGHTWEIGHT_LIMIT:
#     print("pay the heavy fee for luggage being over weight")

# Code auto-formatting: https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8
# Linting: https://marketplace.visualstudio.com/items?itemName=ms-python.flake8


print("Spam" + "spamspam")
print("spam" * 3)
this_string = "f" * 1000
# ' I have eaten ' + 99 + ' burritos.'
' I have eaten ' + str(99) + ' burritos.'

num_burritos = 99
print(f'I have eaten {num_burritos} burritos')

# print('What is your age?') # ask for their age
#    myAge = input() <--- string
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

my_age_int = int(myAge)
my_age_incr = my_age_int + 1
incr_str = str(my_age_incr)
print('You will be ' + incr_str + ' in a year.')

my_addition = True
myfavorcodinggame= True 