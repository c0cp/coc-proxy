### Clash of Clans Client Handler

### Modules

import threading
import coc.connpair
from coc.proxy import Connection
from client.crypto import ClientCrypto

### Classes

class ClientProtocol(threading.Thread):

	# Init

	def __init__(self, sock):

		# Init thread

		threading.Thread.__init__(self)

		# Set local variables

		self._sock = Connection(sock)
		self._cc = ClientCrypto()

		# Start thread

		self.start()

	# Start listen loop in thread

	def run(self):

		threading.Thread(target=self.listen).start()

	# Listen loop

	def listen(self):

		while 1:

			# Check if server is ready

			if not coc.connpair.server:
				continue

			try:

				# Receive data

				data = self._sock.listen()
				if not data: break

				# Decrypt data

				data = self._cc.decryptPacket(data)

				# Split decrypted data into message id, length and payload

				msgid = data[0]
				length = data[1]
				payload = data[2]

				# Call send() function on server
				# where it's gonna be encrypted

				coc.connpair.server.send(msgid, length, payload)

				# Print on screen

				print("R: %s (%s)" % (str(msgid), str(length)))

			except Exception, e:
				print "CLIENT LISTEN: " + str(e)

		# Loop got interupted
		# Disconnect from Supercell Server

		self._sock.close()
		print "Server disconnected."

	# send() function
	# called by Client Handler (Server)

	def send(self, msgid, length, data):

		# Encrypt data for Supercell Server
		# and send

		self._sock.send(self._cc.encryptPacket(msgid, length, data))