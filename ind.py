#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")
    a = {"b", "c", "h", "i", "j"}
    b = {"e", "h", "i", "s", "w"}
    c = {"a", "b", "j", "k", "l", "m"}
    d = {"a", "h", "i", "w", "x"}
    bn = u.difference(b)
    x = (a.difference(c)).intersection(bn)
    print(f"x = {x}")
    y = (a.intersection(bn)).union(c.difference(d))
    print(f"y = {y}")
