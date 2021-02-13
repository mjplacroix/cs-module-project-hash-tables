# lists keep things in order
my_list = []
​
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
​
# why are dictionaries not in order? i.e., order is not guaranteed
## everything hashes differently
## don't know what index the hash function will return
​
my_list = [5, 3, 4, 2, 6, 7, 8, 1, 9]
​
d = {
    'Austin': 12,
    'Michael': 24,
    'Troy': 35,
    'Jorge': 99,
    'David': 42
}
​
# how can we sort our dictionary?
​
# turn into a list
for pair in d.items():
    print(pair)
​
# d.items().sort()
​
print(sorted(d.items()))
​
sorted_list_of_items = list(d.items())
​
def anon_function(pair):
    return pair[1]
​
# sorted_list_of_items.sort(reverse=True, key=anon_function)
sorted_list_of_items.sort(reverse=True, key=lambda pair: pair[1])
​
print(sorted_list_of_items)
​
# Erik's way with list comprehension: sorted([(v, k) for k, v in d.items()])
​
# const my_func = x => x * 2
​
something = list(map(lambda x, y:
    x * 2, [1, 2, 3]))