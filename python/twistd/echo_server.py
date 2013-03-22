from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    
    #protocol.Protocol.
    def connectionMade(self):
        print "Client connected"
    
    def connectionLost(self, data):
        print "Connection was lost"
    
    def dataReceived(self,data):
        self.transport.write(data)
        
class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()
    
reactor.listenTCP(8000,EchoFactory())
reactor.run()

    
