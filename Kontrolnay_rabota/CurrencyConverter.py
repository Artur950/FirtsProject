# Описание логики работы конвертора
# -*- coding: utf-8 -*-
import sys
from Parser import Parser
from Gui_for_convert import Ui_MainWindow
from PyQt5 import QtWidgets


class CurrencyConv(QtWidgets.QMainWindow):
    # Класса конвертера валют будет содержать одно поле,
    # в которое будет передаваться словарь с кодами валют и их курсом
    # из Parser
    current_converted_price = {}

# Метод инициализации объекта CurrencyConv
    def __init__(self):
        # Вызов метода инициализации объекта-родителя
        super(CurrencyConv, self).__init__()
        # Создание объекта типа Parser
        parser = Parser()
        # Получение словаря с кодами валют и их курсами и запись в соответствующее поле
        self.current_converted_price = parser.get_currencies()
        # Создание и инициализация окна графического интерфейса
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

# Метод инициализации окна графического интерфейса
    def init_ui(self):
        # Присвоение заголовка окну приложения
        self.setWindowTitle('Конвертер валют')
        # Внесение списка кодов валют в выпадающий список конвертируемой валюты
        self.ui.comboBox_input.addItems(self.current_converted_price.keys())
        # Поле указания количесво конвертируемой валюты
        self.ui.input_currency.setPlaceholderText('Сколько конвертировать?')

        # Внесение списка кодов валют в выпадающий список
        self.ui.comboBox_output.addItems(self.current_converted_price.keys())
        # Поле в котором отображается полученное количество валюты с учетом курса
        self.ui.output_currency.setPlaceholderText('Сегодня ВЫ получите')
        # Вызов метода конвертации при нажатии на кнопку
        self.ui.convert.clicked.connect(self.converter)

# Метод в котором описано логика конвертации валют
    def converter(self):
        # Чтение значения выбранной валюты для конвертации
        input_currency = self.ui.comboBox_input.currentText()
        # Чтение значения количества выбранной валюты для конвертации
        input_value = self.ui.input_currency.text()

        # Чтение значения выбранной валюты в которую осуществляется конвертация
        output_currency = self.ui.comboBox_output.currentText()
        # Вычисление количества валюты после конвертации с точностью до второго знака после запятой
        output_value = round((float(input_value) * float(self.current_converted_price[input_currency])) \
                       / float(self.current_converted_price[output_currency]), 2)
        # Вывод полученного значения конвертированной валюты в виде строки
        self.ui.output_currency.setText(str(output_value))


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()
sys.exit(app.exec())
