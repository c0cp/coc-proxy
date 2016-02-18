### Clash of Clans Python Proxy Module

### Import module

import socket

## Initialize a connection

class Connection:

	# Set local variables

	def __init__(self, sock):

		self.sock = sock

	# Listen for data for a specific time

	def listen(self):

		try:

			# Receive data

			data = self.sock.recv(65536)
			return data

		except Exception, e:

			# Print error message

			print str(e)

	# Send a message to the socket

	def send(self, msg):

		# Check length of message

		if len(msg) > 0:

			try:

				# Send message

				self.sock.sendall(msg)

			except Exception, e:

				# Print error message

				print "Error Send Data: " + str(e)

	# Close socket

	def close(self):

		self.sock.close()