# create two lists
list1 = []
list2 = []

# create circular reference

list1.append(list2) # list2 referenced by list1
list2.append(list1) # list1 referenced by list2

# even after deletion, lists still reference each other
del list1 # still referenced by list2[0]
del lsit2 # still referenced by list1[0]

# garbage collector detects these objects are unreachable
# memory will be freed in the next GC cycle