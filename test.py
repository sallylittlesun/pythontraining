#!/usr/bin/python
#-*-coding : utf-8 -*-

import os
import  getopt
import sys
import random
from PIL import Image,ImageDraw, ImageFont,ImageFilter
import urllib2
from bs4 import BeautifulSoup

print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf8')  
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
               

def readurl(url):
    page = urllib2.urlopen(url)
#    f = open('source','w')
#    f.writelines(page)
#    f.close()
    return page

def d0008(url):
    page = readurl(url)
    soup = BeautifulSoup(page)    
    f = open('text','w')
    text = soup.get_text()
    f.write(text)
    f.close()

def d0009(url):
    links = []
    page = readurl(url)
    soup = BeautifulSoup(page)
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    print links

def ranchr():
    return chr(random.randint(65,90))

def rancolor1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rancolor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

def d0010():
    width = 240
    height = 60
    image = Image.new('RGB',(width,height),(255,255,255))
    font = ImageFont.truetype('/usr/share/cups/fonts/FreeMono.ttf',42)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in  range(height):
            draw.point((x,y),fill=rancolor1())
    for i in range(4):
        draw.text((60 * i + 10, 10), ranchr(), font=font, fill=rancolor2())
    image = image.filter(ImageFilter.BLUR)
    image.save('randchr.jpg','jpeg')

def d0011(word):
    filist = []
    f = open('filtered_words.txt')
    wlist = f.readlines()
    for i in wlist:
        a = i.strip('\n')
        filist.append(a)
    if word in filist:
        print 'Freedom!'
    else:
        print 'human right!'

def d0012(word):
    filist =map(lambda i: i.strip('\n').decode('utf-8'), open('filtered_words.txt').readlines())
    print filist
    print word
    new = word
    for i in filist:
        if i in word:
            new = new.replace(i,'*'*len(i))
    print new

if __name__=='__main__':
#     d0009('https://github.com/Yixiaohan/show-me-the-code')
    word = raw_input('please input your words:')
    d0012(word)



