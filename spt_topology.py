#!/usr/bin/python 

from mininet.topo import Topo

class MyFirstTopo( Topo ):
     def __init__ ( self ): 
         "Creating custom topology." 
         #Initalize topology 
         Topo.__init__( self ) 
         #Adding nodes, b1-b4 and switch, 1 
         b1 = self.addHost( 'b1' )
         b2 = self.addHost( 'b2' )
         b3 = self.addHost( 'b3' )
         b4 = self.addHost( 'b4' ) 
         Switch = self.addSwitch( 's1' )

         #adding links 
         self.addLink( b1, Switch ) 
         self.addLink( b2, Switch )
         self.addLink( Switch, b3 )
         self.addLink( Switch, b4 )  

topos = { 'myfirsttopo': ( lambda: MyFirstTopo() ) } 
#def runExperiment():
#    "Create and test a simple experiment" 
#    topo = MyFirstTopo( ) 
#    net = Mininet(topo)
#    net.start()
#    print "Dumping host connections"
#    dumpNodeConnections(net.hosts) 
#    print "Testing network connectivity"  
#    net.pingAll()
    #net.stop()

#if __name__ == '__main__':
   #Tell mininet to print useful information 
#   setLogLevel('info') 
#   runExperiment() 
        
