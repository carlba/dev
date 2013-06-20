#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


#http://twistedmatrix.com/documents/current/web/howto/using-twistedweb.html#auto16

from twisted.web import server, resource
from twisted.internet import reactor, threads

import time

class Simple(resource.Resource):
    isLeaf = True    


    def render_GET(self, request):
        d = threads.deferToThread(self.slow_operation, request)
        d.addCallback(self.done,request)
        return server.NOT_DONE_YET
        

    def slow_operation(self,request):
        print "Before sleep"
        time.sleep(5)
        request.write("Calle")
        request.finish()

        return "mupp"

    def done(self,test,request):
        print test
        print "Reached done"
        #request.write("Calle")
        #request.finish()
        return "Done"

    	

site = server.Site(Simple())
reactor.listenTCP(8080, site)
reactor.run()