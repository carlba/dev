import urllib2
from lxml import etree
import codecs
latitude = "59.266158"
longitude = "18.090561"


class Temp:
    def __init__(self):
        self.fname = "temp.xml"
        self.encoding = "utf-8"
        pass
    
    def get_data(self):
        with codecs.open (self.fname, 'w+', self.encoding) as the_file:
            the_file.write(urllib2.urlopen('http://api.temperatur.nu/tnu_1.12.php?lat=%s&lon=%s&amm&verbose&cli=calle12asdasdfasdffasdqedfasdfsdfgsdfrqwer13323333' % (latitude,longitude)).read())    
        
    def load_data(self):
        with open (self.fname, 'r+') as the_file:
            self.reply= the_file.read()
    
    def handle_data(self):
        self.tree = etree.parse(self.reply)
        


def main():
    t = Temp()
    t.get_data()
    t.load_data()
    t.handle_data()
    
    print t.reply
    print t.tree

    

if __name__ == '__main__':
    main()





    
