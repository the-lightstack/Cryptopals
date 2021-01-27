#!/usr/bin/env python3

from bitstring import BitArray,Bits
from operator import itemgetter
from collections import Counter
import string
import re


def score_str(decrypt):
	""" Scores an decrypted text based on the mathing to the english letter mixture. """
	data = ""
	for i in range(2,len((decrypt[2:])),2):
		temp = None
		try:
			temp = bytes.fromhex(decrypt[i:i+2]).decode("ASCII")
		except Exception as e:
			print(decrypt[i:i+2])
			raise e
		if temp:
			data += temp


	score_table =  {'e': 12.70,'t': 9.056,'a': 8.167,'o': 7.507,'i': 6.966,'n': 6.749,'s': 6.327,'h': 6.094,'r': 5.987,
					'd': 4.253,'l': 4.025,'c': 2.782,'u': 2.758,'m': 2.406,'w': 2.360,'f': 2.228,'g': 2.015,'y': 1.974,'p': 1.929,'b': 1.492,
					'v': 0.978,'k': 0.772,'j': 0.153,'x': 0.150,'q': 0.095,'z': 0.074,
					}
	score = 0
	for i in data:
		if score_table.get(i):
			score += score_table.get(i.lower())
	
	return round(score/len(data),10)


def check_sequence(data):
	""" Takes a hex string as input and xor's it with a one byte key.
		The results then get scored as described in the score_str() function above.
	 """

	xor = lambda x,y: hex(int(x,16)^int(y,16))

	outcomes = []
	for i in range(49,127): # One byte = 2^8 = 256 possibilites
		num1 = "0x"+str(((hex(i)[2:]).zfill(2)*int((len(str(data)))/2)))
		out = xor(num1,data)
		outcomes.append([hex(i),score_str(out),out])

	sorted_encr_pairs = sorted(outcomes,key=lambda x: x[1])[::-1]
	# Returns the ten encrypted texts with the key having the best score
	return sorted_encr_pairs[0]


def hamming_distance(str1,str2):
	"""Calculate the hamming distance between two byte strings. """
	bit_str1 = BitArray(str1)
	bit_str2 = BitArray(str2)
	return (Bits("0b"+bit_str2.bin)^Bits("0b"+bit_str1.bin)).count(True)


def breakup_message(message,keysize):
	"""Parses one long bytestream into many pieces each with width of keysize. """
	pieces = []
	for i in range(0,len(message),keysize):
		pieces.append(message[i:i+keysize])
	return pieces


def byte_list_to_hex(byte_list):
	
	result = ""
	for i in byte_list:
		result += hex(i)[2:].zfill(2)
	return "0x"+result


def reorder_blocks(blocks):
	"""Takes first byte of every block and groups them, same for the following bytes. """
	keysize = len(blocks[0])
	rearranged_blocks = [[] for i in range(keysize)]
	for i in blocks:
		for j,data in enumerate(i): # Loops over all bytes in a block
			rearranged_blocks[j].append(data)
	return rearranged_blocks


def cracker():
	"""Crack a repeating key XOR encryption """
	with open("6d.txt","rb") as f:
		encrypted_message = f.read()

	normalized_scores = []
	for keysize in range(2,40): # has to be 40 not 4 
		part1 = encrypted_message[:keysize]
		part2 = encrypted_message[keysize:(keysize*2)]
		part3 = encrypted_message[keysize*2:keysize*3]
		part4 = encrypted_message[keysize*3:keysize*4]
		score = ((hamming_distance(part1,part2)+hamming_distance(part3,part4))/2)/keysize
		normalized_scores.append([score,keysize])
	print("Hamming Sizes:")	
	[print(i) for i in sorted(normalized_scores,key=lambda x:x[0])]
	keysizes = [i[1] for i in sorted(normalized_scores,key=lambda x: x[0])][:5]
	print("-"*30+"\n")
	print("Different possible Keysizes:\n",keysizes,"\n"*2)
	#for ks in keysizes[:5]:#change this BACK!!!

	ks = keysizes[0] #tmp
	# Loop through the first 5 possible key-sizes
	blocks = breakup_message(encrypted_message,ks) 
	arranged_blocks = reorder_blocks(blocks)
	print(f"Cracking sequence for Keysize {ks} ...\nThere are {ks} blocks to be cracked.")
	keys = []
	for i in arranged_blocks:
		hex_block = byte_list_to_hex(i)
		print(hex_block)
		keys.append(check_sequence(hex_block)[0])
	print("Keys:",keys)
	print("ASCII("+"".join([chr(int(i,16)) for i in keys])+")")




if __name__=="__main__":
	cracker()