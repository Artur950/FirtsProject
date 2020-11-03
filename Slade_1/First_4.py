#
def english_russian_dictionary():
    dictionary_english_russian = {"apple": "яблоко",
                                  "age": "возраст",
                                  "answer": "ответ",
                                  "bank": "банк",
                                  "chess": "шахматы",
                                  "humble": "скромный",
                                  "have": "иметь",
                                  "cosmic": "космический",
                                  "cost": "стоить",
                                  "fish": "рыба"}
    print(dictionary_english_russian)
    dictionary_russian_english = {v: k for k, v in dictionary_english_russian.items()}
    print(dictionary_russian_english)
    russian_words_list = [k for k in dictionary_russian_english.keys()]
    print(sorted(russian_words_list))
    english_words_list = [k for k in dictionary_english_russian.keys()]
    print(sorted(english_words_list))


english_russian_dictionary()
