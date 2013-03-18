
from lxml import etree
import urllib2
import urllib
import convertlog
import json
import argparse
from xml.sax.saxutils import escape, unescape
from objprettyprint import object_pretty_print
from collections import defaultdict
from cblib.dictdiffer import DictDiffer

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


class SolicitSender():
    def __init__(self, solcit_object,useragent=None, hostname=None):
        self.solicit_object = {}
        self.solicit_object["data"] = solcit_object
        self.solicit_object["hosname"] = hostname        
        
        if useragent:
            self.useragent = useragent
        else:
            self.useragent = "AliceAutoUpdateAgent"
        if hostname:
            self.hostname = hostname
        else:
            hostname = "defaultvalue"  # oldems
        #hostname = "testdms.stockholm.qa.birdstep.com"
        #hostname = "http://khan.d.birdstep.internal:8000" #newems
        #shorthostname =hostname[hostname.find("/")+2:hostname.find(".")]
        shorthostname = "olddms"
        self.htmldoc=open('result-%s.html' %( shorthostname), 'w+')
        #url = "%s/?xpi=1&xcv=2.9.1.1&xcc=2.9.1.40&xos=WinXP&osid=&xcg=6666&xlg=en&home_network=24001&current_network=24005&imsi=111210000000003&imei=555556666600008&cgmi=Huawei&cgmm=E220&cgmr=FW1&bearer=edge&local_admin_rights=user&guid=D7C19869-A782-4CA1-94CC-F0C6C83F3DB7&apn=apn.birdstep.se&ssid=$SSID$&xun={D9AD9B2D-52F2-4C20-A049-6C91F0A66D83}&mac_address=00:24:E8:98:14:2F&xso=2&test=1'" % (hostname)

    def send_solicit(self, url, useragent):
        req = urllib2.Request(url)
        req.add_header('User-agent', useragent)
        response = urllib2.urlopen(req)
        return response
    
    def handle_solicit_response(self, response):
        html = response.read()
        xmlobject = etree.XML(html)
        
        xmlstring = etree.tostring(xmlobject, pretty_print=True)        
        return xmlobject
        
            

    def retrive_xpath_text(self, response):
        #surl = xmldata.xpath("/AliceAcmAup/RemoteSps/Sp/Url")
        #surl = xmldata.xpath("/AliceAcmAup/RemoteSps/Sp")
        #print surl[0].text
        #return surl[0].text
        pass


    def write_html(self):
        self,htmldoc.write("<html> \n")
        self,htmldoc.write("<body> \n")
        self.htmldoc.write("<pre> \n")
        
        self.htmldoc.write("\n")
        self.htmldoc.write(tc)
        self.htmldoc.write("\n")
        
        self.htmldoc.write("\n</pre>")
        self.htmldoc.write("\n</body>")
        self.htmldoc.write("\n</html>")    
    
    
    def do_work(self):
              
        result = {}
        result["hostname"] = self.hostname
        result["data"] = {}
        
        for tc in self.solicit_object["data"]:            
            for urldict in self.solicit_object["data"][tc]:
                urlparams = urllib.urlencode(urldict)
                url = "%s/?%s" % (self.hostname,urlparams)
                self.htmldoc.write("\n" + url + "\n")
                response = self.send_solicit(url, self.useragent)
                xmldata = self.handle_solicit_response(response)
                
                result["data"][tc] = {}                
                result["data"][tc]["xml"] = (xmldata)
                result["data"][tc]["dict"] = (etree_to_dict(xmldata))
                result["data"][tc]["url"] = url
                
                #xmldata = retrive_xpath_text(xmldata)
                #self.htmldoc.write(escape(xmldata))
                #self.htmldoc.write(xmldata)  
        
        return result
        
    


class SolicitComparer():
    def __init__(self, solicit_result1,solicit_result2):
        self.solicit_result1 = solicit_result1
        self.solicit_result2 = solicit_result2
        self.output=open('result-%s.txt' %("replace"), 'w+')        
        self.write_output("===================================================")
        hoststring = "Diff between %s and server %s" % ( self.solicit_result1["hostname"], self.solicit_result2["hostname"])
        self.write_output(hoststring )
        self.write_output("===================================================")

    
    def nodetoset(self, node):
        rellist = []        
        releases= node.findall("RemoteSps/*")        
        for release in releases:                                    
            #print release.values()
            #print release.find("Filename").text
            #print release.find("ReleaseId").text
            rellist.append(release.find("ReleaseId").text)
            pass
        #print rellist
        return rellist
    
    def findparent(self, node, tagname, text):
        rellist = []        
        releases= node.findall("RemoteSps/*")        
        for release in releases:                                                
            if release.find("ReleaseId").text == text:
                return release.find("ReleaseId").getparent()
        return None
            
        #print rellist
        
    def print_host_result(self,data,hostname,url,id):        
        parent = self.findparent(data,"ReleaseId", id)
        self.write_output("===================================================")
        self.write_output(hostname)
        self.write_output(url)
        if parent:                            
            self.write_output(etree.tostring(parent))
        else:
            self.write_output("No matches")

    def compare(self):
        
        if not (set(self.solicit_result1.keys()) - set(self.solicit_result2.keys())): #The testcases are the same.
            
            for tc in self.solicit_result1["data"]:
                rellist1 = self.nodetoset(self.solicit_result1["data"][tc]["xml"])
                rellist2 = self.nodetoset(self.solicit_result2["data"][tc]["xml"])                
                
                #print rellist1
                #print rellist2
                
                #difference = set(rellist1) - set(rellist2)
                
                difference = set(rellist1) ^ set(rellist2)
                
                print difference
                if difference:
                    print difference
                    for id in difference:                      
                        parent = self.findparent(self.solicit_result1["data"][tc]["xml"],"ReleaseId", id)
                        
                        self.write_output("===================================================")
                        self.write_output(tc)
                            
                        self.print_host_result(self.solicit_result1["data"][tc]["xml"],self.solicit_result1["hostname"], self.solicit_result1["data"][tc]["url"],id)
                        self.print_host_result(self.solicit_result2["data"][tc]["xml"],self.solicit_result2["hostname"],self.solicit_result1["data"][tc]["url"],id)
                        

        else:       
           print "The testcases executed for the different resultsets must be the same"
    
    def write_output(self,text):        
        if text:
            self.output.write(text + "\n")
        
        
       
            
            
            
        
        
        
        
        
        
        #print dictdiff.unchanged()
        
        #print self.solicit_result1
        #print self.solicit_result1["AliceAcpAup"]["Sp"]
    

        
        
            
    


def etree_to_dict(t):
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.iteritems():
                dd[k].append(v)
        d = {t.tag: {k:v[0] if len(v) == 1 else v for k, v in dd.iteritems()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.iteritems())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
              d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d

    
def main():    
    with open("test.json", 'r') as f:
        solobj = json.loads(f.read())
    
    solicitsender1 = SolicitSender(solobj,useragent="AliceAutoUpdateAgent", hostname = "https://khan.d.birdstep.internal")   
    result1 = solicitsender1.do_work()
    #print result1
    

    
    #testdict = result1["Clientgroup 1000 Homenetwork 22222"]["dict"]
    
    #object_pretty_print(test)
    
    #object_pretty_print(testdict)
    
    #print test["AliceAcpAup"]["Sp"]
    
    
    
    
    
    solicitsender2 = SolicitSender(solobj,useragent="AliceAutoUpdateAgent", hostname = "http://khan.d.birdstep.internal:8080")   
    result2 = solicitsender2.do_work()
    
    solcomp = SolicitComparer(result1, result2 )
    solcomp.compare()   
 
    
    
    pass

if __name__ == '__main__':
    main()




# REtrive filename of releases
#xmlobject= xmlobject.findall("RemoteSps/Sp")
#        
#        for release in xmlobject:
#            self.htmldoc.write(release.find("Filename").text)


#sys.exit()




#urlparams = urllib.urlencode(urldict)
#url = "%s/?%s" % (hostname,urlparams)
##url = "https://cygni.ems.birdstep.com/?xpi=1&xcg=7777&xso=2&xcv=1.2.249&xos=drd40&xlg=eng&imei=A0000030C08CB4&imsi=310009134653799&cgmi=samsung&cgmm=prevail2spr&cgmr=prevail2spr-eng+4.0.4+IMM76I+M830VPALK6+test-keys&home_network=311870&current_network=311870&mac_address=1C%3A62%3AB8%3AAA%3AFF%3AC6&local_admin_rights=admin&test=1"
##print url
#
#fcounter = 0
#kcounter = 0
#
#counterdict = {}




    

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
