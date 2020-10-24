def alist(args):
    pass


def delete_empty_tuple():
    aList = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    print(aList)
    for i in reversed(range(len(alist))):
        if alist[i][0] == 0:
            alist.pop(i):
        else:
            print(i)
    print(aList)


delete_empty_tuple()