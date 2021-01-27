#!/usr/bin/env python3

from bitstring import BitArray, Bits


def hamming_distance(str1,str2):
	"""Calculate the hamming distance between two byte strings. """
	bit_str1 = BitArray(str1)
	bit_str2 = BitArray(str2)
	return (Bits("0b"+bit_str2.bin)^Bits("0b"+bit_str1.bin)).count(True)

def main():
	data = b"35371f1652102c4c0e4e0a3a181618067f1a0a1c1e7f090101123803450d0e7f170901167f1f1a1e1730191159007f1a0a1c1e7f070a17472c044530413c170b520a3a094f07017f061c590832060917143a021b0f1336040b590e3956111a1c7f040e030a360502590536051113173c094f07147f080a0b133a15115c"
	#key = "a_very_long_key"
	key_pairs = []
	#Start of by trying different keys
	for i in range(2,40):
		# i being one keysize
		p1 = data[0:i]	
		p2 = data[i:(i*2)]	
		h_dist = hamming_distance(p1,p2)
		key_pairs.append([h_dist/i,i])
	[print(i) for i in sorted(key_pairs,key=lambda x:x[0])]
def main2():
	def breakup_message(message,keysize):
		"""Parses one long bytestream into many pieces each with width of keysize. """
		pieces = []
		for i in range(0,len(message),keysize):
			pieces.append(message[i:i+keysize])
		return pieces	
	def reorder_blocks(blocks):
		"""Takes first byte of every block and groups them, same for the following bytes. """
		keysize = len(blocks[0])
		rearranged_blocks = [[] for i in range(keysize)]
		for i in blocks:
			for j,data in enumerate(i): # Loops over all bytes in a block
				rearranged_blocks[j].append(data)
		return rearranged_blocks
	def byte_list_to_hex(byte_list):
		result = ""
		for i in byte_list:
			result += hex(i)[2:].zfill(2)
		return "0x"+result

	temp = breakup_message("This is a long text and I want to control whether it produces quality or trash",4)
	print("Blocks:",temp)
	order_temp = (reorder_blocks(temp))	
	for i in order_temp:
		print(i)
	print(([i.encode() for i in order_temp[0]]))
if __name__=="__main__":
	main2()
