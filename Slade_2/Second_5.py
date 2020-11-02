# Написали программу которая проверяет является ли одно слово аннаграммой второго
def is_anagram(word1, word2):
    if len(word1) == len(word2):
        if sorted(word1) == sorted(word2):
            print('True')
        else:
            print('False')
    else:
        print('Слова не равны по длинне!')


is_anagram("коон", "окно")
