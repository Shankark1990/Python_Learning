my_list = [1, 2, 3]

# Indexing
print("Element of index 0 is:", my_list[0])

# Changing an element
my_list[1] = 10
print("List after changing an element at index 1: ", my_list)

# append()
my_list.append(200)
print("List after append", my_list)

# extend()
my_list.extend([3, 400])
print("List after extend", my_list)

# insert
my_list.insert(1, 'A')
print("List after inserting element", my_list)

# remove
my_list.remove('A')
print("List after removing", my_list)

# Copy list
my_copy_list = my_list.copy()
print(my_copy_list)

# clear list
my_list.clear()
print(my_list)
print(my_copy_list)

# sort a list
my_copy_list.sort()
print("List after sorting", my_copy_list)

# Reverse a list
my_copy_list.reverse()
print("List after reversing", my_copy_list)
