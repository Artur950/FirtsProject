def search_in_strings(word1, word2):
    common_letters = set(word1) & set(word2)
    print(common_letters)


search_in_strings("literature", "architect")
