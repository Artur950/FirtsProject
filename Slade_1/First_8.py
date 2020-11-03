# Написали программу удаляющую дублирующие пары в словаре
def dictionary():
    dictionary = {"apple": "яблоко",
                  "age": "возраст",
                  "answer": "ответ",
                  "bank": "банк",
                  "chess": "шахматы",
                  "apple": "яблоко",
                  "age": "возраст",
                  "answer": "ответ",
                  "answer": "ответ",
                  "age": "возраст",
                  "cost": "стоить",
                  "age": "возраст"}
    print(sorted(dictionary.items()))



dictionary()
