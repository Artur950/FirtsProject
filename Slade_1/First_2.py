# Напечатали функцию которая проверяет что все элементы кортежа одинаковые
def compare():
    tupl_1 = (45, 45, 45, 45)
    print(tupl_1)
    if tupl_1[0] == tupl_1[1] and tupl_1[0] == tupl_1[2] and tupl_1[0] == tupl_1[3]:
        print(True)
    else:
        print(False)


compare()