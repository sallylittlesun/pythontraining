#!/usr/bin/python
#-*- coding : utf-8 -*-

import os
import re
from  collections import Counter
import urllib2



def get_word(file):
    with open(file) as f:
#        text = f.read().split()
        pattern = r'''[A-Za-z]+|\$?\d+%?$'''
        text = re.findall(pattern,f.read())
    print text
#    for i in range(len(text)):
#        a = text[i]
#        if a.endswith('.') or a.endswith(';') or a.endswith('?') or a.endswith(','):
#            text[i] = a[:1]
    new_words = delnonwords(text)

def delnonwords(words):
    stop_word = ['the','your','you','he','she','in','of','and','to','has','that','s','is','are','a','with','as','an','for']
    cword = Counter(words)
    for i in stop_word:
        print '%s---%d'%(i,cword[i])
        cword[i]=0
    print cword.most_common()[0][0]
    return words

if __name__=='__main__':
    get_word('urlib2.txt')
