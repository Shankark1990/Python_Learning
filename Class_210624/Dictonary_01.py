# Dictionary is a collection of key and value
# Dictionary is unorder collection.
# Dictionary will not keep the insertion order
# OrderDict will keep the insertion order.


my_dict = {
    "name": "Shankar",
    "isMale": True
}

print(my_dict["name"])
print(my_dict.get("name"))
print(my_dict.values())
print(my_dict.keys())

check_dupl = {'a': 1, 'w': 3, 'c': 5, 'b': 23}
print(check_dupl)
print(len(check_dupl))  # dictornary duplicate key doesn't allow

for i in check_dupl.keys():
    print('Key:', i)
for i in check_dupl.values():
    print('value:', i)
for k, v in check_dupl.items():
    print('Key:', k, 'Value:', v)

from collections import OrderedDict

od = OrderedDict()
od['a'] = 23
od['w'] = 24
od['b'] = 22
od['d'] = 54
od['c'] = 93

print(od)
