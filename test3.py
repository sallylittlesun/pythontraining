#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import time

def test3():
# x+100=n^2  n^2+168=m^2  m=n+k 代入可得n=85/k-1/2*k
    for i in range(1,13):
        n = 84/i - 0.5*i
        m = 84/i + 0.5*i
        if int(n) == n:
            l1 = m*m-268
            l2 = n*n-100
            if l1 == l2:
                print "++++"
                print n,m

def test4(d):
    ydate = time.strptime(d,'%Y-%m-%d').tm_yday #time模块自带属性可以获取一些时间上的数值
    print ydate
    return ydate

def test5(x):
    num = x.split(',')  #用split分割的字符串形成的列表中的各个部分还是字符串
    num2 = [int(n) for n in num]
    num2.sort()
    print num2

if __name__=='__main__':
#    test3()
#    d = raw_input('input the date in XXXX-XX-XX:')
#    test4(d)
    x = raw_input('input 3 numbers,split with ",":')
    test5(x)
