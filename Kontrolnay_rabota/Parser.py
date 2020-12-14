# -*- coding: utf-8 -*-
import requests  # Модуль для обработки URL
from bs4 import BeautifulSoup  # Модуль для работы с HTML

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/87.0.4280.66 Safari/537.36'}
address_bank_of_russia = 'http://www.cbr.ru/scripts/XML_daily.asp'

name_currencies = []


def get_list_currencies():
    # Парсим всю страницу
    resp = requests.get(address_bank_of_russia, headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(resp.content, 'xml')
    char_code_currencies = soup.find_all('CharCode')
    value_currencies = soup.find_all('Value')
    # Список кодов валют
    list_currencies = []
    for i in char_code_currencies:
        list_currencies.append(i.get_text())
    # Список с курсом валют
    list_value = []
    for j in value_currencies:
        # Добавляем в конец списка по одному значению, приведенному
        # к типу float и округленного до 2 знаков после запятой
        list_value.append(round(float(j.get_text().replace(",", ".")), 2))
    dict_currencies = {key: value for key, value in zip(list_currencies, list_value)}
    # Очищаем списки, ведь они нам больше не нужны
    list_value.clear()
    list_currencies.clear()
    # В итоге функция вернет созданный нами словарь
    return dict_currencies


get_list_currencies()