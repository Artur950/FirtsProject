import PySimpleGUI as simple_gui
from Konvertor_valut import Currency


def create_window():
    currency = Currency()
    layout = [[simple_gui.Text('Цена за 1 доллар равна ' + currency.check_currency_USD())],

            [simple_gui.InputText()],
            [simple_gui.InputText()],
            [simple_gui.Submit(), simple_gui.Cancel()]]

    window = simple_gui.Window('КУРС ВАЛЮТ', layout)

    event, values = window.read()
    window.close()


create_window()
