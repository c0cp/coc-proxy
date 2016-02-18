### Clash of Clans Proxy
### Version: 0.1
### Author: c0cp
### Last modified: Thu, 18 Feb 2016

### Modules

import socket
import coc.connpair as proxy
from server.protocol import ServerProtocol
from client.protocol import ClientProtocol

### Variables

CHOST = "gamea.clashofclans.com"
CPORT = 9339

SHOST = ""
SPORT = 9339

### Main script

print "Proxy started."

# Initialize server socket

ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssock.bind((SHOST, SPORT))
ssock.listen(1)

# Wait for clients

print "Waiting for client ... ",

conn, ip = ssock.accept()

print "connected!"

# After client has connected
# initialize socket to Supercell Server

print "Initialize socket ... ",

try:

	csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	csock.connect((CHOST, CPORT))
	print "done!"

except Exception, e:

	print "failed!"
	print str(e)
	raw_input("\nPress any key to exit ...")
	exit()


print "Handle client and server now."


try:

	# Start threads

	proxy.server = ServerProtocol(conn)
	proxy.client = ClientProtocol(csock)

	proxy.server.run()
	proxy.client.run()

	# Endless loop 

	while 1:
		continue

except Exception, e:

	print "Could not start threads."
	print str(e)
	raw_input("\nPress any key to exit ...")
	exit()