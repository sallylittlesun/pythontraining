#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import os

def test40():
    l = [1,6,3,7,'a','b','e']
    l.reverse()
    print l

def test56():
    from Tkinter import *
 
    canvas = Canvas(width=800, height=600, bg='yellow')  
    canvas.pack(expand=YES, fill=BOTH)                
    k = 1
    j = 1
    for i in range(0,26):
        canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=1)
        k += j
        j += 0.3
 
    mainloop()

def test67(l):
    l = l.split(',')
    l = [int(i) for i in l]
    print l
    maxnum = l.index(max(l))
    print max(l),maxnum
    minnum = l.index(min(l))
    print min(l),minnum
#    l[maxnum],l[0] = l[0],l[maxnum] #l列表从0开始
#    l[minnum],l[-1] = l[-1],l[minnum]
    for i in range(len(l)):
        if l[i] == max(l):
            l[i],l[0] = l[0],l[i]
    for i in range(len(l)):
        if l[i] == min(l):
            l[i],l[-1] = l[-1],l[i]
    print l

def test69(n):
    l = []
    for i in range(1,n):
        
        if i % 3 == 0:
            l.append(3)
        elif i % 2 == 0 and i % 3!= 0:
            l.append(2)
        else:
            l.append(1)
    print l
    for i in range(len(l)):
        if l[i] != 3:
            print i

def test98(s):
    s = s.swapcase()
    f = open('test','w')
    f.write('%s'%s)
    f.close()

def test99():#list.sort() sorted()的 区别
    a = open('a','r')
    sa = a.read()
    a.close()
    b = open('b','r')
    sb = b.read()
    b.close()
    c = sorted('%s'%(sa+sb))
    f = open('c','w')
    f.write('%s'%c)
    f.close()
     


if __name__=='__main__':
#    test56()
#    s = raw_input('input alpha :')
    test99()
