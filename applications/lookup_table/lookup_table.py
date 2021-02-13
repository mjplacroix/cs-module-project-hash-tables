# Your code here
import math
import random
import time

start = time.time()

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


# build a cache of factorial 1 - 36 of range of random options below
factorials = {}

# iterate through each multiplied result of both ranges
for i in range(2, 14):
    for s in range(3, 6):
        powers = math.pow(i, s)
        print(f'{i, s} == {powers}')
        factorials[powers] = math.factorial(powers)

# compute the factorial
# store as a key:value - multiple:factorial 

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here

    # copy/pasted code from above
    v = int(math.pow(x, y))

    # reference your cache for the factorial
    v = factorials[v]
    v //= (x + y)
    v %= 982451653



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

end = time.time()
print(end - start)
