#!/usr/bin/python
#-*-coding : utf-8 -*-

import os
import xlwt
import re
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

def d0014():
    f = xlwt.Workbook(encoding = 'utf-8')
    studentsht = f.add_sheet('student')
    pattern = re.compile(r'"(\d+)":\["(.*?)",(\d+),(\d+),(\d+)]')
    ftxt = open('student.txt')
    j = 0
    for line in ftxt.readlines():
        print line
        print pattern.findall(line)
        choose = pattern.findall(line)
        if choose:
            for i in range(len(choose[0])):
                studentsht.write(j,i,choose[0][i]) 
            j +=1
    ftxt.close()
    f.save('student.xls')
    f.close()

def d0015():
    f = xlwt.Workbook(encoding = 'utf-8')
    citysht = f.add_sheet('city')
    pattern = re.compile(r'"(\d+)" : "(.*?)"')
    lines = pattern.findall(open('city.txt').read())
    print lines
    i = 0
    for x in lines:
        for j in range(len(x)):
            citysht.write(i,j,lines[i][j])
        i += 1
    f.save('city.xls')

if __name__=='__main__':
    d0015()
