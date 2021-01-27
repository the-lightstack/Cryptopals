#!/usr/bin/env python3

import string


real = "This is a normal english sentence, and I just noticed that sentences that are longer"
fake = "And another sentence to be debunked or not, lets see"

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

def score(user_in):
	global score_table
	score = 0
	data = user_in.lower()
	letter_chars = "".join(list(filter(lambda x: x in string.ascii_letters,user_in)))
	for i in string.ascii_lowercase:
		amount = data.count(i)
		actual_percent = (data.count(i)/len(data))*100
		diff = abs(score_table[i]-actual_percent)
		score += diff
	#Stil have to normalize it
	return score/len(letter_chars)

real_score = round(score(real),4)
fake_score = round(score(fake),4)
# Low score means normal sentence, so real
print(f"Real\t|\tFake\n{'-'*20}\n{real_score}\t|\t{fake_score}")

print("\nThe actal english sentence was: ")
print("---------------------------------")
print(real) if real_score<fake_score else print(fake)
'''
frequ_e = score_table["e"]
actual_freq_e = (real.count("e")/len(real))*100
print("Actual Frequency for e:",actual_freq_e)
diff = abs(frequ_e-actual_freq_e)
print("Difference:",diff)
'''