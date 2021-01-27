#!/usr/bin/env python3
from bitstring import BitArray
from time import sleep
import sys
def main():
	def xor_byte(data,key):
		return "0x"+hex(data^key)[2:].zfill(2)
		
		
	verbose = "-v" in sys.argv[1:] 
	decrypt = "-d" in sys.argv[1:]
	file_path = None
	if "-f" in sys.argv[1:]:
		file_path = sys.argv[sys.argv.index("-f")+1]
		print("file path:",file_path)

	if "-h" in sys.argv[1:]:
		print("Usage: "+str(__file__)+" <flags>")
		print("Flags: -d (Decrypt), -v (Verbose and really cool), -f <file_path>")
		exit(0)
	if decrypt and file_path is None:
		plain_text = BitArray("0x"+input("Hex String > "))
	elif file_path is not None and decrypt:
		with open(file_path,"rb") as f:
			content = f.read()
		plain_text = BitArray(content)
	else:
		plain_text = BitArray(input("Plaintext String > ").encode("ascii")) #If it doesn't work, that could be because of wrong formating

	key = BitArray(input("Your Key > ").encode("ascii"))
	output = BitArray()

	key_counter = 0
	print("key len",len(key.bytes))
	for i in plain_text.bytes:
		# First do operation
		
		temp = xor_byte(i,key.bytes[key_counter])
		
		if verbose: print(f"\033[1;32m Key:\033[0m {key.bytes[key_counter]}\t\033[1;32mData byte:\033[0m {i}\t\033[1;32mXOR outcome:\033[0m {temp}\r",end="")

		output += (temp)
		key_counter = (key_counter +1) % len(key.bytes)
		
		if verbose: sleep(len(plain_text)/16000)
	print()
	print("\033[0;32m"+"―"*45+"\033[0m\n")
	print(output.hex)



if __name__=="__main__":
	main()

