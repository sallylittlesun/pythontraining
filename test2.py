#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import xlwt
import xlrd
import re
import sys
import xml.dom.minidom as dom

reload(sys)
sys.setdefaultencoding('utf8')
print sys.getdefaultencoding()

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

def d0016():
    f = xlwt.Workbook(encoding='utf-8')
    nsheet = f.add_sheet('number')
    pattern = re.compile(r'\[(\d+), (\d+), (\d+)]')
    print pattern.findall(open('number.txt').read())
    lines = pattern.findall(open('number.txt').read())
    j = 0
    for line in lines:
        for i in range(len(line)):
            nsheet.write(j,i,line[i])
        j += 1
    f.save('number.xls')

def get_data(xls):
    data = xlrd.open_workbook(xls)
    table = data.sheet_by_name('student')
    dic = {}
    for i in range(table.nrows):
        print str(table.row_values(i)[1].decode('utf-8'))
#        content = content +'    '+ table.row_values(i)[0] +' : '+ str(table.row_values(i)[1:]) ',\n'
        
        dic[table.row_values(i)[0]]=table.row_values(i)[1:]
    print dic
    return dic

def d0017(xls):
    doc = dom.Document()
    root = doc.createElement('root')
    student = doc.createElement('student')
    doc.appendChild(root)
    root.appendChild(student)
    a = '学生信息表\n "id" : [名字, 数学, 语文, 英文]'
    comment = doc.createComment(a)
    student.appendChild(comment)
    content = get_data(xls)
    student.appendChild(doc.createTextNode(str(content)))
    f = open('student.xml','w')
    f.write(doc.toprettyxml(encoding = 'utf-8'))

if __name__=='__main__':
    d0017('student.xls')
