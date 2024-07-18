t = (23, 34, 54)
print(t)

new_tuple = t + (5,)
print(new_tuple)

my_list = list(new_tuple)  # tuple to list
print(my_list)
my_list.append(45)
new_t2 = tuple(my_list)  # list to tuple
print(new_t2)
