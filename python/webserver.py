
#http://twistedmatrix.com/documents/current/web/howto/using-twistedweb.html#auto16

from twisted.web import server, resource
from twisted.internet import reactor

import time

class Simple(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html>Calle</html>"

site = server.Site(Simple())
reactor.listenTCP(8080, site)
reactor.run()