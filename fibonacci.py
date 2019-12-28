#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# Fibonacci series
# sum of two ele come to the next number

a,b = 0,1
while (b< 10): 
    print(b, end=',')
    a,b = b,a+b

print (b)
