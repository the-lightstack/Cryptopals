#!/usr/bin/env python3


def score_str(decrypt):
	""" Scores an decrypted text based on the mathing to the english letter mixture. """

		try:
			bytes_obj = bytes.fromhex(decrypt[2:])
			decrypt = bytes_obj.decode("ASCII") # This code throw errors too
		except Exception as e:
			with open("errors.log","a") as f:
				f.write(e+"\n"*2)
			return -1
		
		score_table =  {'e': 12.70,'t': 9.056,'a': 8.167,'o': 7.507,'i': 6.966,'n': 6.749,'s': 6.327,'h': 6.094,'r': 5.987,'d': 4.253,'l': 4.025,
						'c': 2.782,'u': 2.758,'m': 2.406,'w': 2.360,'f': 2.228,'g': 2.015,'y': 1.974,'p': 1.929,'b': 1.492,
						'v': 0.978,'k': 0.772,'j': 0.153,'x': 0.150,'q': 0.095,'z': 0.074,
						}
		score = 0
		
		for i in decrypt:
			if score_table.get(i):
				score += score_table.get(i.lower())
		
		return round(score,10)


def check_sequence(data):
	global contents

	# Takes two hexadecimal numbers and returns the xor output of both
	xor = lambda x,y: hex(int(x,16)^int(y,16))

	outcomes = []
	for i in range(256): # One byte = 2^8 = 256 possibilites
		num1 = "0x"+str((hex(i)[2:]*30))
		#num2 = data
		out = xor(num1,data)
		outcomes.append([hex(i),score_str(out),out,contents.index(data)])

	#contains the	
	pretty_res = sorted(outcomes,key=lambda x: x[1])[::-1]
	pretty_res = pretty_res
	return pretty_res


def main():
	with open("4.txt","r") as f:
		contents = f.read()

	contents = contents.split("\n") # Big list of encrypted strings

	big_data = []
	for row in contents:
		big_data.append(check_sequence(row))

	long_data = []
	for line in big_data:
		for obj in line:
			if obj[1]>0:
				long_data.append(obj)

	print("lenght of long data:",len(long_data))
	parsed_long_data = sorted(long_data,key=lambda x:x[1])[::-1]
	for i in parsed_long_data[:20]:
		ascii_representation = bytes.fromhex(i[2][2:]).decode("ASCII")
		print(f"Key: {i[0]}\tLine: {i[3]}\tScore: {i[1]}\tText: {ascii_representation}")


if __name__=="__main__":
	main()