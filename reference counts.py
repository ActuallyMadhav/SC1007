import sys # importing module

# create list and first reference
x = [1,2,3] # reference count = 1
# print current reference count minus 1 as getrefcount() creates a temporary reference
print(sys.getrefcount(x)-1) # output: 1
# memory state: one reference (x) pointing to [1,2,3]

# add second reference
# create another reference y pointing to the same list object
y = x # reference count = 2
print(sys.getrefcount(y)-1) # output: 2
# memory state: two references (x,y) pointing to [1,2,3]

# add third reference
# create a third reference z pointing to the same list object
z = x # reference count = 3
print(sys.getrefcount(z)-1) # output: 3
# memory state: three references (x,y,z) pointing to [1,2,3]

# delete x reference
del x # reference count = 2
# memory state: refcount decreases to 2
# two references remain (y,z) pointing to [1,2,3]

# delete y reference
del y # reference count = 1
# memory state: refcount decreases to 1
# one reference remains (z) pointing to [1,2,3]

# delete z reference
del z # reference count = 0
# memory state: refcount becomes 0
# no references remain, object is now elligible for garbage collection (refcount must be 0)

# garbage collection not typically needed tho, python automatically handles cleanup and returns number of objects collected
