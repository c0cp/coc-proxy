### Clash of Clans Crypto Libary

### Import modules

import struct
from coc.utils import from_bytes, to_bytes
from pyblake2 import blake2b
import nacl.utils
from nacl.public import PrivateKey, PublicKey, Box

### Classes

## En/Decryption Box

class CryptoBox:

	# Init

	def __init__(self, sk=None, pk=None):

		# Set local Variables

		self._box = None

		self.sk = None
		self.pk = None

		# Generate key pair if nessessary

		if not sk or not pk:

			self.sk = PrivateKey.generate()
			self.pk = self.sk.public_key

		else:

			self.sk = sk
			self.pk = pk

		# Generate shared key / box

		self._box = Box(self.sk, self.pk)

	# Encryption

	def encrypt(self, plaintext, nonce=None):

		if not nonce:
			nonce = nacl.utils.random(Box.NONCE_SIZE)

		ciphertext = self._box.encrypt(plaintext, nonce)
		return ciphertext[24:]

	# Decryption

	def decrypt(self, ciphertext, nonce=None):

		if nonce:
			plaintext = self._box.decrypt(ciphertext, nonce)
		else:
			plaintext = self._box.decrypt(ciphertext)

		return plaintext


## Nonce generator

class Nonce:

	# Initialize variables

	def __init__(self, serverkey=None, clientkey=None, nonce=None):

		if not clientkey:

			if nonce:

				self._nonce = nonce

			else:

				self._nonce = nacl.utils.random(Box.NONCE_SIZE)

		else:

			b2 = blake2b(digest_size=24)

			if nonce:
				b2.update(bytes(nonce))

			b2.update(bytes(clientkey))
			b2.update(bytes(serverkey))
			
			self._nonce = b2.digest()

	# Function, that is called when Nonce() gets called by bytes()

	def __bytes__(self):
		return self._nonce

	# Function, that is called when Nonce() gets called by len()

	def __len__(self):
		return len(self._nonce)

	# Increase nonce

	def increment(self):
		
		# Python 3.x method from clugh
		#
		# self._nonce = (int.from_bytes(self._nonce, byteorder="little") + 2).to_bytes(Box.NONCE_SIZE, byteorder="little")

		# Python 2.x method
		# using coc.utils

		self._nonce = to_bytes(from_bytes(self._nonce, byteorder="little") + 2, byteorder="little")
