#!/usr/bin/env python3


def xor(num1,num2):
	'''
	Data has to be passed in in the format: 0x<hex_data>
	'''
	from bitstring import BitArray
	num1 = BitArray(num1)
	num2 = BitArray(num2)
	def bit_xor(b1,b2):
		return int((b1 or b2 ) and not(b1 and b2))
	#print("Num1:",num1.bin)
	#print("Num2:",num2.bin)
	r=""
	for i in range(num1.len):
		r+=(str(bit_xor(int(num1.bin[i]),int(num2.bin[i]))))
	return hex(int(r,2))


if __name__ =="__main__":

	num1 = "0x1c0111001f010100061a024b53535009181c"
	num2 = "0x686974207468652062756c6c277320657965"
	print(xor(num1,num2))