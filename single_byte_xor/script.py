#!/usr/bin/env python3

from operator import itemgetter
from collections import Counter
import string
import re


def score_str(decrypt):
	cleaned_decrypt = re.sub("[\x00-\x19\x7f-\xff]","",decrypt)

	bytes_obj = bytes.fromhex(cleaned_decrypt[2:])
	string_decrypt = bytes_obj.decode("ASCII") # This code throw errors too

	
	score_table =  {'e': 12.70,
					't': 9.056,
					'a': 8.167,
					'o': 7.507,
					'i': 6.966,
					'n': 6.749,
					's': 6.327,
					'h': 6.094,
					'r': 5.987,
					'd': 4.253,
					'l': 4.025,
					'c': 2.782,
					'u': 2.758,
					'm': 2.406,
					'w': 2.360,
					'f': 2.228,
					'g': 2.015,
					'y': 1.974,
					'p': 1.929,
					'b': 1.492,
					'v': 0.978,
					'k': 0.772,
					'j': 0.153,
					'x': 0.150,
					'q': 0.095,
					'z': 0.074,}
	score = 0
	print(string_decrypt)
	counts = Counter(string_decrypt.lower())

	letter_chars = "".join(list(filter(lambda x: x in string.ascii_letters,string_decrypt)))
	print(letter_chars)
	for i in counts:
		if i not in string.ascii_letters:
			continue
		#print(score_table[i]," - ",len(letter_chars),"/",counts[i],"=",score_table[i]-len(letter_chars)/counts[i])
		#bad_score += (abs(score_table[i]-len(letter_chars)/counts[i]))/len(letter_chars)
	
		#		always 0<			0 =<	 always positive
		print("part1:",len(letter_chars)/counts[i])
		score += ((len(letter_chars)/counts[i]))-score_table[i]
	print("Scoring: ",score)
	print("Scoring: ",score)
	return score


def score(decrypt):
	cleaned_decrypt = re.sub("[\x00-\x19\x7f-\xff]","",decrypt)

	bytes_obj = bytes.fromhex(cleaned_decrypt[2:])
	user_in = bytes_obj.decode("ASCII") # This code throw errors too

	
	score_table =  {'e': 12.70,
					't': 9.056,
					'a': 8.167,
					'o': 7.507,
					'i': 6.966,
					'n': 6.749,
					's': 6.327,
					'h': 6.094,
					'r': 5.987,
					'd': 4.253,
					'l': 4.025,
					'c': 2.782,
					'u': 2.758,
					'm': 2.406,
					'w': 2.360,
					'f': 2.228,
					'g': 2.015,
					'y': 1.974,
					'p': 1.929,
					'b': 1.492,
					'v': 0.978,
					'k': 0.772,
					'j': 0.153,
					'x': 0.150,
					'q': 0.095,
					'z': 0.074,}

	score = 0
	data = user_in.lower()
	letter_chars = "".join(list(filter(lambda x: x in string.ascii_letters,user_in)))
	for i in string.ascii_lowercase:
		amount = data.count(i)
		actual_percent = (data.count(i)/len(data))*100
		diff = abs(score_table[i]-actual_percent)
		score += diff
	return score/len(letter_chars)
def main():
	xor = lambda x,y: hex(int(x,16)^int(y,16))


	data = "0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736 "
	#data = "0x0b1f011d540c1a00170a161f0d1e000f4107334e481965021f093b3a100f0b0e0a5342564f4e495352135e0049410f1747484d65011106223024085200650d0b5b000305070715070001384e0a440108310e170e3a3c060a140d184c454e2a4e060706111d5900001d2759094a2a0e11473c37100c061a4f00455f004e08070113054e171307044c071f651b1547743613491d1b0749174d414e495319540600076b4e0b00060c0b4f546d30361149521903520c1a536408073b1d16071d040a0100091f621a19407378046306490a43081a423708531c1b065717410d00001b40360603002d2c080052491849451a00640f531d541e4e06140f45001c4d3602110878081063" #temporary


	outcomes = []
	for i in range(49,127): # One byte = 2^8 = 256 possibilites
		# Below line just parses `i` to be xor-ready
		num1 = "0x"+str(((hex(i)[2:]).zfill(2)*int(len(data)/2)))
		
		#num2 = data
		out = xor(num1,data)
		outcomes.append([hex(i),score_str(out),out])


	print("[*] Program finished running\n"+"-"*30)
	pretty_res = sorted(outcomes,key=itemgetter(1))
	print("Len of outcomes:",len(outcomes))
	for i in pretty_res[:10]:
		
		print("Key:",i[0],"\tScore:",i[1],"\tEncrypted Text:",bytes.fromhex(i[2][2:]).decode("ASCII"))

if __name__=="__main__":
	main()