#!/usr/bin/env python3

from operator import itemgetter
from collections import Counter


def score_str(decrypt):
	length = len(decrypt)
	try:
		bytes_obj = bytes.fromhex(decrypt[2:])
		decrypt = bytes_obj.decode("ASCII") # This code throw errors too
	except:
		return -1
	#eotha
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
	try:
		#print("Decrypt:",decrypt+"\r",end="")
		for i in decrypt:
			if score_table.get(i):
				score += score_table.get(i)
		
	except Exception as e:
		# Maybe it results in some none-unicode chars?
		print("Couldn't loop over the string\n{}".format(e))
	return round(score/length,3)

	# Takes two hexadecimal numbers and returns the xor output of both
def main():
	xor = lambda x,y: hex(int(x,16)^int(y,16))


	data = "0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	#data = "0x1d0f4e1f131b002033060d0c1e111a1d09530c0100474509081f62411a741a7a3a1a1d014131060b491b074e070854191669020701021b36544e3b0f001c544f0c0e3d490d0e0b074e0b001f4d0e41474f420c062a5907310a591d130e0b04301c1a0852135c0f2c07191b2a024f160817650019353a49010d160000301a622052114e060b171d65474a414510132e4e6474034152000a09093049060207105f1d4553404f4e084d0a061d21004e3c4e4352110e0c0831061b0417001a4e06164d1b414700080117484c3d3a3d4e3615071605360606491336554e451d4d0259284113191b23500d211a59171b410a41361b070a1d111a1d0a531443454b00040c2127570f3b014e521d65450d3b1918041b15534e0a070c4f4f060045071d294f173507540054062c123408070613011a1b0d160c1d4347001c0c042352002d1a4e1d35070d412c064f1a17134d490853053f536d50161b19054e07350a54131c010a6b3d0618491b3d4f0b421d0c0e000f4e02005236791c3001415213073c08300007191c541a01044b4d067940531c4907354e08740f00061d000a41310607491c181a0a45120948006d530000176263013a02642b110c45157849480c17001a06113a090a434700061c1d2c4e0b3537411011421c4d2f491d1c063d1a424954081d2a084e000d16255309354e00520d061c413d451f491518521b0853050d470e4f0a101c62490a2d1a4b011d0000312c0f480a17541a0200010c0e4e12574510136e003e200800111d4f00163908061c52111a4e261c020141064e1063" #temporary


	outcomes = []
	for i in range(49,127): # One byte = 2^8 = 256 possibilites
		# Below line just parses `i` to be xor-ready
		num1 = "0x"+str(((hex(i)[2:]).zfill(2)*int(len(data)/2)))
		print(num1)
		#num2 = data
		out = xor(num1,data)
		outcomes.append([hex(i),score_str(out),out])


	print("[*] Program finished running\n"+"-"*30)
	pretty_res = sorted(outcomes,key=itemgetter(1))[::-1]
	print("Len of outcomes:",len(outcomes))
	for i in pretty_res[:10]:
		
		print("Key:",i[0],"\tScore:",i[1],"\tEncrypted Text:",bytes.fromhex(i[2][2:]).decode("ASCII"))

if __name__=="__main__":
	main()