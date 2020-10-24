aList = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
bList = [x for x in aList if x != ()]
print(bList)
