# Написали программу преобразующую список кортежей в словарь
def tuple_list():
    list_of_tuples = [("Первый", 1), ("Второй", 2), ("Третий", 3), ("Четвертый", 4), ("Пятый", 5), ("Шестой", 6)]
    result_dictionary = dict(list_of_tuples)
    print(result_dictionary)


tuple_list()