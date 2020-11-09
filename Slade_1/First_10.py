# Напишите программу удаляющую пересечение второго набора из первого набора
def delete_intersection():
    a_set = {i * 2 for i in range(10)}
    b_set = {i * 3 for i in range(10)}
    print(a_set)
    print(b_set)
    intersection_list = sorted(a_set.intersection(b_set))
    result_set = {i for i in a_set if i not in intersection_list}
    print(result_set)


delete_intersection()