
from lxml import etree
import urllib2
import urllib
import convertlog
import json
import argparse
from xml.sax.saxutils import escape, unescape

import sys

#Junk

#Commandline
#parser = argparse.ArgumentParser(prog='solicitgen')
#
#parser.add_argument("test")
#
#arguments = parser.pvars(arse_args());

#Convertlog
#urldict = convertlog.HTTPGetToObj(url)

#Save to file
#
#with open("x.txt", 'w+') as f:
#   f.write(urlstring)
#




useragent = "AliceAutoUpdateAgent"
#hostname = "testdms.stockholm.qa.birdstep.com"
#hostname = "http://khan.d.birdstep.internal:8000" #newems
hostname = "http://khan.d.birdstep.internal:8080" #oldems

#shorthostname =hostname[hostname.find("/")+2:hostname.find(".")]

shorthostname = "olddms"


htmldoc=open('result-%s.html' %( shorthostname), 'w+')
#url = "%s/?xpi=1&xcv=2.9.1.1&xcc=2.9.1.40&xos=WinXP&osid=&xcg=6666&xlg=en&home_network=24001&current_network=24005&imsi=111210000000003&imei=555556666600008&cgmi=Huawei&cgmm=E220&cgmr=FW1&bearer=edge&local_admin_rights=user&guid=D7C19869-A782-4CA1-94CC-F0C6C83F3DB7&apn=apn.birdstep.se&ssid=$SSID$&xun={D9AD9B2D-52F2-4C20-A049-6C91F0A66D83}&mac_address=00:24:E8:98:14:2F&xso=2&test=1'" % (hostname)


def send_solicit(url, useragent):
    req = urllib2.Request(url)
    req.add_header('User-agent', useragent)
    response = urllib2.urlopen(req)
    return response

def handle_solicit_response(response):
    html = response.read()
    xmlobject = etree.XML(html)    
    xmlobject= xmlobject.findall("RemoteSps/Sp")
    
    for release in xmlobject:
        htmldoc.write(release.find("Filename").text)
    
    #print xmlobject


    #xmldata = etree.tostring(xmlobject)
    
    #return xmldata


def retrive_xpath_text(response):
    #surl = xmldata.xpath("/AliceAcmAup/RemoteSps/Sp/Url")
    #surl = xmldata.xpath("/AliceAcmAup/RemoteSps/Sp")
    print surl[0].text
    return surl[0].text


def main():
    htmldoc.write("<html> \n")
    htmldoc.write("<body> \n")
    htmldoc.write("<pre> \n")
    
    
    with open("test.json", 'r') as f:
        urlset = json.loads(f.read())
    
    for tc in urlset:
        htmldoc.write("\n")
        htmldoc.write(tc)
        htmldoc.write("\n")
        for urldict in urlset[tc]:
            urlparams = urllib.urlencode(urldict)
            url = "%s/?%s" % (hostname,urlparams)
            response = send_solicit(url, useragent)
            xmldata = handle_solicit_response(response)
            #xmldata = retrive_xpath_text(xmldata)
            #htmldoc.write(escape(xmldata))
            #htmldoc.write(xmldata)
            htmldoc.write("\n")
            
    htmldoc.write("\n</pre>")
    htmldoc.write("\n</body>")
    htmldoc.write("\n</html>")
if __name__ == '__main__':
    main()


sys.exit()

urlparams = urllib.urlencode(urldict)
url = "%s/?%s" % (hostname,urlparams)
#url = "https://cygni.ems.birdstep.com/?xpi=1&xcg=7777&xso=2&xcv=1.2.249&xos=drd40&xlg=eng&imei=A0000030C08CB4&imsi=310009134653799&cgmi=samsung&cgmm=prevail2spr&cgmr=prevail2spr-eng+4.0.4+IMM76I+M830VPALK6+test-keys&home_network=311870&current_network=311870&mac_address=1C%3A62%3AB8%3AAA%3AFF%3AC6&local_admin_rights=admin&test=1"
#print url

fcounter = 0
kcounter = 0

counterdict = {}




    

#
#for i in range(0,100000):
#    req = urllib2.Request(url)
#    req.add_header('User-agent', useragent)
#    response = urllib2.urlopen(req)
#
#    html = response.read()
#    xmlbec = etree.XML(html)
#    #print etree.tostring(xmlbec);
#    surl = xmlbec.xpath("/AliceAcmAup/RemoteSps/Sp/Url")
#    print surl[0].text
#
#    counterHostname = surl[0].text[0:surl[0].text.find(".com")+4]
#
#    if counterHostname in counterdict:
#        counterdict[counterHostname] += 1
#    else:
#        counterdict[counterHostname] = 0
#
#    print counterdict




#for i in range(0,100):
#    req = urllib2.Request(surl[0].text)
#    req.add_header('User-agent', useragent)
#    req.add_header('Range', 'bytes=%s-%s' % (0, 2))
#    response = urllib2.urlopen(req)
#    html = response.read()
#    print html
#    req = urllib2.Request(surl[0].text)
#    req.add_header('User-agent', useragent)
#    response = urllib2.urlopen(req)
#    html = response.read()
#    response.close()
#    print html
#print html
