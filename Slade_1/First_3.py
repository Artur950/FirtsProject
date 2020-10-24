def delete_empty_tuple():
    aList = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    print(aList)
    resultList = [i for i in aList if i != ()]
    print(resultList)


delete_empty_tuple()
