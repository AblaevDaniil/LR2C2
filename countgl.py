#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    text = list(input("Введите текст: "))
    number = 0
    for char in ["а","е","о","ё","у","и","ы","э","ю","я"]:
        number += text.count(char)
    print(number)