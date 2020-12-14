# -*- coding: utf-8 -*-
import Parser


class Currency:
    current_converted_price = {}

    def __init__(self):
        # Установка курса валюты при создании объекта
        self.current_converted_price = Parser.get_list_currencies()

    def check_currency(self):
        for k in self.current_converted_price.keys():
            print('1 ' + str(k) + ' стоит ' + str(self.current_converted_price[k]))
            # return '1 ' + str(k) + ' стоит ' + str(self.current_converted_price[k])


# Создание объекта и вызов метода
currency = Currency()
currency.check_currency()