import random
import inspect

number = [1,2,3,4,5]

random_numbers = [3,7,2,1,5,9]
print(sorted(random_numbers))
print(random_numbers)

tuples_prices = [
   ('product1', 10),
   ('product2', 5),
   ('product3', 15)
]

numbers = list(map(lambda item: item[0], tuples_prices))
numbers_prices = [price for price in tuples_prices] # remember the variable need same name.

filter_numbers = list(filter(lambda item: item[1] >= 10, tuples_prices))
filter_items = [price[1] for price in tuples_prices if price[1] >= 10]

print(filter_items)



