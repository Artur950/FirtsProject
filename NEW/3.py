# -*- coding: utf-8 -*-
import re


def camel_to_snake(string_source):
    print(string_source)
    pattern = re.compile('(?!^)([A-Z]+)')
    str_result = pattern.sub(r'_\1', string_source).lower().replace(' _', ' ')
    print(str_result)


camel_to_snake('MyVar17 = OtherVar + YetAnother2Var '
               'TheAnswerToLifeTheUniverseAndEverything = 42')