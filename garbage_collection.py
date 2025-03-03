import gc

list1 = [1,2,3]
list2 = [4,5,6]

list1.append(list2)
list2.append(list1)

del list1
del list2

gc.collect()


print(list1)
print(list2)