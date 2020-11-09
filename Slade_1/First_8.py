# Написали программу удаляющую дублирующие пары в словаре
# Полная
def dictionary():
    dictionary = {"apple": "яблоко",
                  "age": "возраст",
                  "answer": "ответ",
                  "bank": "банк",
                  "chess": "шахматы",
                  "apple": "яблоко",
                  "answer": "ответ",
                  "answer": "ответ",
                  "age": "возраст",
                  "cost": "стоить",
                  "age": "возраст"
                  }
    print(sorted(dictionary.items()))
    print(dictionary.__sizeof__())
    set_keys = set()
    for i in dictionary.keys():
        set_keys.add(i)
    result_dictionary = dict.fromkeys(sorted(set_keys))
    for j in dictionary:
        for z in result_dictionary:
            if j == z:
                result_dictionary[z] = dictionary[j]
    print(result_dictionary.items())
    print(result_dictionary.__sizeof__())


dictionary()
