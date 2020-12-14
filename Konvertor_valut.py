import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
class Currency:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.66 Safari/537.36'}
    address_bank_of_russia = 'http://www.cbr.ru/scripts/XML_daily.asp'
    current_converted_price = []

    def __init__(self):
        # Установка курса валюты при создании объекта
        self.current_converted_price = float(self.get_currency_price().replace(",", "."))

    def get_currency_price(self):
        # Парсим всю страницу
        resp = requests.get(self.address_bank_of_russia, headers=self.headers)
        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(resp.content, 'xml')
        convert_USD = soup.find('CharCode', text='USD').find_next_sibling('Value').string
        # convert_EUR = soup.find('CharCode', text='EUR').find_next_sibling('Value').string

        # current_exchange_rate = (convert_USD, convert_EUR)
        return convert_USD

    # def create_dictionary_currency(self):
    #    dict_currency = {}
    #    dict_currency = dict.fromkeys(soup.find('CharCode').string)


    def check_currency_USD(self):
        print('Доллар США равен ' + str( self.current_converted_price))
        return str(self.current_converted_price)

# Создание объекта и вызов метода
#currency = Currency()
#currency.check_currency()