a = lambda x: x * 2
print(a(2))
collection = [1, 2, 3, 4, 5]
coll = [x * 2 for x in collection if x % 2 == 0]
print(coll)
coll_1 = [x * 2 if x % 2 else x * 10 for x in collection]
print(coll_1)
collaboration = [x + y for x in collection for y in coll_1 if x % 2 and not y % 2]
print(collaboration)

# sets
set_col = {x for x in collection}
print(set_col)

# dicts
dict_col = {x: x**2 for x in collection}
print(dict_col)
