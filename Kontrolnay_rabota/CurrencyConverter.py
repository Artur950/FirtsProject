# -*- coding: utf-8 -*-
import sys
from Parser import Parser
from Gui_for_convert import Ui_MainWindow
from PyQt5 import QtWidgets


class CurrencyConv(QtWidgets.QMainWindow):
    current_converted_price = {}

    def __init__(self):
        super(CurrencyConv, self).__init__()
        parser = Parser()
        self.current_converted_price = parser.get_currencies()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Конвертер валют')

        self.ui.comboBox_input.addItems(self.current_converted_price.keys())
        self.ui.input_currency.setPlaceholderText('Сколько конвертировать?')

        self.ui.comboBox_output.addItems(self.current_converted_price.keys())
        self.ui.output_currency.setPlaceholderText('Сегодня ВЫ получите')
        self.ui.convert.clicked.connect(self.converter)

    def converter(self):
        input_currency = self.ui.comboBox_input.currentText()
        input_value = self.ui.input_currency.text()

        output_currency = self.ui.comboBox_output.currentText()
        output_value = round((float(input_value) * float(self.current_converted_price[input_currency])) \
                       / float(self.current_converted_price[output_currency]), 2)
        self.ui.output_currency.setText(str(output_value))


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()
sys.exit(app.exec())
