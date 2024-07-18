set1 = {"hello", "Test", "hello."}
for i in set1:
    print(i)

set2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 11])
print(len(set2))
set2.remove(0)  # remove item from set.
print(set2)
set2.add(100)  # add item to set
print(set2)

set2.pop()  # remove the first item from set
print(set2)
