### Clash of Clans Server Crypto Handler

### Import modules

from coc.crypto import CryptoBox, Nonce
from coc.data import Data
from nacl.public import PrivateKey, PublicKey

### Classes

## Main class

class ServerCrypto:

	# Init

	def __init__(self):

		# Set local variables

		self._sk = PrivateKey(("f1f5b312fbd5066eed4c025d041218fded694fe07dea458953ca56cf3bd46e5f").decode("hex"))
		self._pk = self._sk.public_key
		self._ck = None

		self._s = None
		self._k = None

		self._nonce = None
		self._snonce = None
		self._rnonce = None

	# Decrypt packet

	def decryptPacket(self, packet):

		# Get message id and payload
		
		data = Data(packet)
		data.unpack()

		msgid = data._msgid
		length = data._length
		payload = data._payload

		# Handle message ids

		if msgid == 10100:

			# Packet 10100 is not encrypted
			# return values

			return msgid, length, payload

		elif msgid == 10101:

			# Packet 10101 is important for further en/decryption

			# Extract clientkey and ciphertext

			self._ck = PublicKey(payload[:32])
			ciphertext = payload[32:]

			# Create temporary CryptoBox

			self._nonce = Nonce(self._pk, self._ck)
			self._s = CryptoBox(self._sk, self._ck)

			# Decrypt client-encrypted data and extract snonce

			plaintext = self._s.decrypt(ciphertext, bytes(self._nonce._nonce))
			self._snonce = Nonce(nonce=plaintext[24:48])

			# Return decrypted message

			return msgid, length, plaintext[48:]

		else:

			# Increment snonce by 2

			self._snonce.increment()

			# Decrypt ciphertext

			ciphertext = payload
			plaintext = self._k.decrypt(ciphertext, self._snonce._nonce)

			# Return plaintext

			return msgid, length, plaintext

	# Encrypt packet

	def encryptPacket(self, msgid, length, payload):

		# Handle message ids

		if msgid == 20100:

			# Packet 20100 is not encrypted
			# Make packet and return

			packet = Data(payload)
			packet.pack(msgid, length)

			return packet._data

		elif msgid == 20103 or msgid == 20104:

			# Packet 20103 may contain updates update files
			# Packet 20104 is important for further en/decryption
			# Encryption is simelar

			# Generate a nonce using blake2b with pk, clientkey and snonce

			self._nonce = Nonce(self._pk, self._ck, self._snonce)

			# Generate rnonce

			self._rnonce = Nonce()

			# Create CryptoBox

			self._k = CryptoBox()

			# Set plaintext

			plaintext = self._rnonce._nonce + bytes(self._k._box) + payload
				
			# Encrypt plaintext using previously generated CryptoBox

			ciphertext = self._s.encrypt(plaintext, self._nonce._nonce)

			# Pack packet and return

			packet = Data(ciphertext)
			packet.pack(msgid, length)

			return packet._data

		else:

			# Increment rnonce by 2

			self._rnonce.increment()

			# Encrypt plaintext

			plaintext = payload
			ciphertext = self._k.encrypt(plaintext, bytes(self._snonce._nonce))

			# Pack packet and return

			packet = Data(ciphertext)
			packet.pack(msgid, length)

			return packet._data