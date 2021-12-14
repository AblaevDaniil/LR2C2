#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    stroka1 = input("Введите первую строку ")
    stroka2 = input("Введите вторую строку ")

    obs = set(stroka1).intersection(set(stroka2))
    print (obs)