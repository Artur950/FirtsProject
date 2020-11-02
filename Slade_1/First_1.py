# Распаковали a_tuple = (10, 20, 30, 40) в 4 переменные и напечатали их
def print_hi():
    a_tuple = (10, 20, 30, 40)
    print(a_tuple)

    a = a_tuple[0]
    b = a_tuple[1]
    c = a_tuple[2]
    d = a_tuple[3]

    print(a, b, c, d)


print_hi()