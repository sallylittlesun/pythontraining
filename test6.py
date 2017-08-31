#!/usr/bin/python
# --*- coding: utf-8 -*--

import os
import sys
import string


def test17(s):
    a = 0 #字母
    n = 0 #数字
    space = 0
    o = 0 #其他字符
    for i in s:
        if i.isalpha():
            a += 1
        if i.isdigit():
            n += 1
        if i == " ":
            space += 1
    o = len(s)-a-n-space
    print '字母：%d,数字：%d,空格：%d,其他：%d'%(a,n,space,o)

def test18(s):
    l = []
    T = 0
    n = int(s.split(',')[0])
    a = int(s.split(',')[1])
    for i in range(1,n+1):
        T += a
        l.append(T)
        a = a * 10
    sum = reduce(lambda x,y:x+y,l)
    print sum    

def test21():
    y = 1
    for i in range(1,10):
        x = 2*(y + 1)   #x是当天剩下的桃子数
        y = x
    print x

def test23(n):
    print n
    if n % 2 != 0:
        for i in range(0,(n/2+1)):
            print ' '*(n/2-i) + '*'*(2*i+1)
        for i in range((n/2+2),n+1):
            print  ' '*(i-n/2-1) + '*'*(2*(n-i)+1)
    else:
        print "input odd!"

def test23o(n):
    for i in range(0,n):
        a = abs(i - int(n/2))
        b = n - abs(i - int(n/2))
        print(" "*a+"*"*(b-a))


if __name__=='__main__':
#    s = raw_input('input string:')
#    test17(s)
#    s = raw_input('input n,a,split with ,:')
#    test18(s)
#    test21()
    n = int(input('input n:'))
    test23o(n)
