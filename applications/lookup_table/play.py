import math
import time

start = time.time()

factorials = {}

# iterate through each multiplied result of both ranges
for i in range(2, 14):
    for s in range(3, 6):
        powers = math.pow(i, s)
        print(f'{i, s} == {powers}')
        factorials[powers] = math.factorial(powers)

print("factorials")




end = time.time()
print(end - start)