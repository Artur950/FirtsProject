# -*- coding: utf-8 -*-
import re


def remove_duplicates():
    str_source = 'Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. Смешно, ' \
                 'не не правда ли? Не нужно портить хор хоровод. '
    print(str_source)
    pattern = re.compile(r'\b([^\W\d_]+)(\s+\1)+\b', flags=re.I)
    str_result = pattern.sub(r'\1', str_source)
    print(str_result)


remove_duplicates()
