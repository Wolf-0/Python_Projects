import string
import hashlib

#unmd5 recursively loop trough alphabeth
# and compare possible hashes return matching string
def unmd5(prefix, max_length, hash):
	if(hashlib.md5(prefix.encode('utf-8')).hexdigest() == hash):
		return prefix
	
	for c in list(string.ascii_letters):
		if len(prefix) < max_length:
			result = unmd5(prefix + c, max_length, hash)
			if result is not None:
				return result


print(unmd5('', 4, "f92bfc75d481c196c1e4deecf7fac3af"))
