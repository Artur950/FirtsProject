def delete_empty_tuple():
    aList = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    print(aList)
    for i in aList:
        if len(i) == 0:
            aList.remove(i)
        else:
            print(i)
    print(aList)


delete_empty_tuple()
