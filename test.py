#!/usr/bin/python
#-*-coding : utf-8 -*-

import os
import  getopt
import sys
from PIL import Image,ImageDraw, ImageFont,ImageFilter

ds1={'width':80,'height':80,'file':''}

def usage():
    print "usage: python test.py -f filepath -w width -e height"
    print "-h --help\n"
    print "-f --file\n"
    print "-w --width\n"
    print "-e --height\n"
    sys.exit(-1)

def options(argv,ds1):
    strings = 'w:e:f:'
    lists = ['help','width=','height=','file=']
    try:
        opts,argv=getopt.getopt(argv,strings,lists)
        print 1
    except getopt.GetoptError,err:
        print 22
        usage()
        sys.exit(-1)
    for o,a in opts:
        if o in ('-h','--help'):
            usage()
        if o in ('-e','--height'):
            ds1['height'] = a
        if o in ('-w','--width'):
            ds1['width'] = a
        if o in ('-f','--file'):
            ds1['file'] = a

def filterp():
    im = Image.open('pikaqiu.jpeg')
    im2 = im.filter(ImageFilter.SHARPEN)
    im2.show()
    im2.save('smooth.jpeg','jpeg')

def d000():
    im = Image.open('edge.jpeg')
    w,h = im.size
    wdraw = 0.8*w
    hdraw = 0.2*h
    Font1 = ImageFont.truetype('/usr/share/cups/fonts/FreeMono.ttf',48)
    drawObject = ImageDraw.Draw(im) 
    drawObject.ink = 255 + 0 * 256 + 0 * 256 * 256 
    drawObject.text((wdraw,hdraw),'4',font=Font1)
    del drawObject
    im.save('numbim.jpeg','jpeg')
if __name__=='__main__':
    d000()

