#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Fibonacci series
# sum of two ele come to the next number

a,b = 0,1
while (b< 10): 
    print(b, end=',')
    a,b = b,a+b

print (b)
