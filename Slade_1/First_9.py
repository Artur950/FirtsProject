# Напишите программу складывающую значения в списке словарей
# [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Counter({'item1': 1150, 'item2': 300})

def counter():
    original_list_of_dictionaries = [{'item': 'item1', 'amount': 400},
                                     {'item': 'item2', 'amount': 300},
                                     {'item': 'item1', 'amount': 750},
                                     ]
    set_keys = set()
    for i in original_list_of_dictionaries:
        set_keys.add(list(i.values())[0])
    dict_counter = dict.fromkeys(sorted(set_keys))
    for j in dict_counter:
        dict_counter[j] = 0

    for i in original_list_of_dictionaries:
        for k in dict_counter.keys():
            if i['item'] == k:
                dict_counter[k] += i['amount']
    print(dict_counter)


counter()
