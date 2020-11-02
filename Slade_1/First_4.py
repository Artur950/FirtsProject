def english_russian_dictionary():
    dictionary = {"apple": "яблоко",
                  "age": "возраст",
                  "answer": "ответ",
                  "bank": "банк",
                  "chess": "шахматы"}
    print({v:k for k, v in dictionary.items()})
    dictionary2 = {"apple": "яблоко",
                  "age": "возраст",
                  "answer": "ответ",
                  "bank": "банк",
                  "chess": "шахматы"}
    dictionary2.update(dictionary)
    print(dictionary)


english_russian_dictionary()
