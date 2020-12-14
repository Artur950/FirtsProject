# -*- coding: utf-8 -*-
import re


def obfuscation(str_source):
    print(str_source)
    nums = re.findall(r'\d+', str_source)
    result_nums = [(int(i)) ** 3 for i in nums]
    for i in range(0, len(nums)):
        str_source = str_source.replace(nums[i], str(result_nums[i]))
    print(str_source)


obfuscation('Было закуплено 12 единиц техники по 410.37 рублей')