# -*- coding: utf-8 -*-
import re


def search_mail():
    my_str = "Иван Иванович! Нужен ответ на письмо от ivanoff@ivan-chai.ru. Не забудьте поставить в копию " \
             "serge'o-lupin@mail.ru- это важно. "
    emails = re.findall("([a-zA-Z0-9_.'+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+)", my_str)
    for mail in emails:
        print(mail)


search_mail()
