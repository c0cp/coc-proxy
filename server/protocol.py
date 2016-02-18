### Clash of Clans Server Handler

### Modules

import threading
import coc.connpair
from coc.proxy import Connection
from server.crypto import ServerCrypto

### Classes

class ServerProtocol(threading.Thread):

	# Init

	def __init__(self, sock):

		# Init thread

		threading.Thread.__init__(self)

		# Set local variables

		self._sock = Connection(sock)
		self._sc = ServerCrypto()

		# Start thread

		self.start()

	# Start listen loop in thread

	def run(self):

		threading.Thread(target=self.listen).start()

	# Listen loop

	def listen(self):

		while 1:

			# Check if client is ready

			if not coc.connpair.client:
				continue

			try:

				# Receive data

				data = self._sock.listen()
				if not data: break

				# Decrypt data

				data = self._sc.decryptPacket(data)

				# Split decrypted data into message id, length and payload

				msgid = data[0]
				length = data[1]
				payload = data[2]

				# Call send() function on client
				# where it's gonna be encrypted

				coc.connpair.client.send(msgid, length, payload)

				# Print on screen

				print("S: %s (%s)" % (str(msgid), str(length)))

			except Exception, e:
				print "SERVER LISTEN: " + str(e)

		# Loop got interupted
		# Disconnect client

		self._sock.close()
		print "Client disconnected."

	# send() function
	# called by Supercell Server Handler (Client)

	def send(self, msgid, length, data):

		# Encrypt data for client
		# and send

		self._sock.send(self._sc.encryptPacket(msgid, length, data))