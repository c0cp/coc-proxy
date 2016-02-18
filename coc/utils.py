### Python 2.7 Implementation of not-native functions

def from_bytes(obj, byteorder):
	
	if byteorder == "big":
		return int(obj.encode("hex"), 16)

	elif byteorder == "little":
		return int("".join(reversed(obj)).encode("hex"), 16)

def to_bytes(obj, byteorder):

	rtn = hex(obj)

	if len(rtn) > 1 and rtn[0:2] == "0x":
		rtn = rtn[2:]

	if len(rtn) > 0 and rtn[-1:] == "L":
		rtn = rtn[:-1]

	if len(rtn) % 2:
		rtn = "0" + rtn

	if byteorder == "big":
		return bytes(rtn.decode("hex"))

	elif byteorder == "little":
		return bytes("".join(reversed(rtn.decode("hex"))))