t = ("hello", "test", "hello")
print(set(t))

set1 = {1, 2, 3}
set2 = {4, 5, 6}
union_set = set1.union(set2)
print("Union set:", union_set)

set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8, 9}
intersection_set = set3.intersection(set4)
print("Intersection set:", intersection_set)

diff_set = set3.difference(set4)
print(diff_set)

diff1_set = set4.difference(set3)
print(diff1_set)
