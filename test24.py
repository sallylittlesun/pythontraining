#!/usr/bin/python
#-*-coding: utf-8 -*-

import os
import sys

def test24():
    a = 1.0 #如果a = 1的话，b/a所得的都是整数，会取整
    b = 2.0
    sum = 0.0
    for i in range(1,21):
        sum = sum + b/a
        temp = b + a
        a = b
        b = temp
        print sum
    print sum

def test28():
    a = 10
    for i in range(1,5):
        b = a + i*2
    print b

def test29(n):  # input()出来的是整数，raw_ipnut出来的是字符串
    l = list(n)
    print len(l)
    print l 
    print l.reverse()

if __name__=='__main__':
#    test24()
#    test28()
    n = raw_input('input a number:')
    test29(n)    
