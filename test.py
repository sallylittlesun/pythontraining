#!/usr/bin/python
#-*-coding : utf-8 -*-

import os
import  getopt
import sys
import random
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

def d0001():
    l = []
    for i in range(1,201):
        l.append(random.randint(1,999))
    print l 

def d0004():
    words,sentenses = 0 , 0
    f = open('en_file.txt')
    for line in f.readlines():
        sentenses += 1
        words += len(line.split())
    print words,sentenses

def d0005(path):
    hight,width = 1136,640
    for dirpath,dirnames,filenames in os.walk(path):
        for f in filenames:
            if f.endswith('.jpg') or f.endswith('.jpeg'):
                fpath = os.path.join(dirpath,f)
                print fpath
                im = Image.open(fpath)
                resizeim = im.resize((width,hight),Image.ANTIALIAS)
                cname = f.split('.')[0]+'_re'+f.split('.')[1]
                resizeim.save('%s'%(cname),'jpeg')
                del resizeim
                fw,fh = im.size
#                if fh < hight and fw > width:
#                    cw = fh*width/hight
#                    ch = fh
#                elif fh > hight:
#                    ch = hight
#                    cw = 
                
            
    

if __name__=='__main__':
    d0005('/home/repo/pythontraining')


