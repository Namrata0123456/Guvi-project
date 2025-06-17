people = [
    {'name': 'Payel', 'age': 25},
    {'name': 'Puja', 'age': 15},
    {'name': 'Priyanka', 'age': 30},
    {'name': 'Rumi', 'age': 12}]


adults = list(filter(lambda person: person['age'] >= 18, people))

adult_names = list(map(lambda person: person['name'], adults))

print(adult_names)

###########
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)

print(product)

#########

numbers = [1, 2, 3, 4]
Obj = lambda x: x % 2 == 0

squares_of_evens = [x**2 for x in numbers if Obj(x)]

print(squares_of_evens)
################
number = lambda s:s.isdigit()

print(number("1234"))
print(number("12ab"))

##########

from datetime import datetime

now = datetime.now()

extract = lambda dt: (dt.year, dt.month, dt.day)

print(extract(now))
######
from functools import reduce

fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1]) if n > 1 else [0][:n]

print(fibonacci(10))
