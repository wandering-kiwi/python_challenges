#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:58:40 2020

@author: avni_aaron
"""

print([("fizzbuzz" if (i%5==0) else ("fizz")) if (i%3==0) else ("buzz" if (i%5==0) else (i)) for i in range(1, 101)])