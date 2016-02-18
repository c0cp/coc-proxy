### Clash of Clans Client Crypto Handler

### Import modules

from coc.crypto import CryptoBox, Nonce
from coc.data import Data
from nacl.public import PrivateKey, PublicKey, Box

### Classes

## Main class

class ClientCrypto:

	# Init

	def __init__(self):

		# Set local variables

		self._pk = None
		self._sk = None
		self._hk = PublicKey(("01c98c143a840d92ee656996dad5af41de5d1b8ebb289081368b5cfda9bd4a30").decode("hex"))

		self._k = None

		self._bk = None

		self._nonce = None
		self._snonce = None
		self._rnonce = None

	# Decrypting

	def decryptPacket(self, packet):

		# Get message id and payload

		data = Data(packet)
		data.unpack()

		msgid = data._msgid
		length = data._length
		payload = data._payload

		# Handle message ids

		if msgid == 20100:

			# Packet 20100 contains a 24-byte string
			# and is not encrypted

			# Extract session key (bk) and return values

			self._bk = payload[-24:]
			return msgid, length, payload

		elif msgid == 20103 or msgid == 20104:

			# Login Failed / OK packet

			# Generate nonce

			self._nonce = Nonce(self._hk, self._pk, bytes(self._snonce._nonce))

			# Generate shared key / cryptobox

			self._s = CryptoBox(self._sk, self._hk)

			# Decrypt payload

			ciphertext = payload
			plaintext = self._s.decrypt(ciphertext, bytes(self._nonce._nonce))

			# Extract rnonce and k

			self._rnonce = Nonce(nonce=plaintext[:24])
			self._k = Box.decode(plaintext[24:56])

			# Return message id and plaintext

			return msgid, length, plaintext[56:]

		else:

			# Increment rnonce by 2

			self._rnonce.increment()

			# Decrypt plaintext

			print msgid

			ciphertext = payload

			plaintext = self._k.decrypt(ciphertext, bytes(self._snonce._nonce))

			# Return plaintext

			return msgid, length, plaintext

	# Encrypting

	def encryptPacket(self, msgid, length, payload):

		# Handle message ids

		if msgid == 10100:

			# Packet 10100 is not encrypted
			# Pack packet and return

			packet = Data(payload)
			packet.pack(msgid, length)

			return packet._data

		elif msgid == 10101:

			# Login packet

			# Generate random snonce

			self._snonce = Nonce()

			# Generate keypair

			self._sk = PrivateKey.generate()
			self._pk = self._sk.public_key

			# Generate nonce using public key (pk) and serverkey (hk)

			self._nonce = Nonce(self._hk, self._pk)

			# Generate shared key

			self._s = CryptoBox(self._sk, self._hk)

			# Encrypt packet

			plaintext = bytes(self._bk) + bytes(self._snonce._nonce) + bytes(payload)
			
			ciphertext = self._s.encrypt(plaintext, bytes(self._nonce._nonce))

			# Pack packet and return

			packet = Data(bytes(self._pk) + ciphertext)
			packet.pack(msgid, length)

			return packet._data

		else:

			# Increment snonce by 2

			self._snonce.increment()

			# Encrypt plaintext

			plaintext = payload
			ciphertext = self._k.encrypt(plaintext, bytes(self._snonce._nonce))

			# Pack packet and return

			packet = Data(ciphertext)
			packet.pack(msgid, length)

			return packet._data