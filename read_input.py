# with open('latin_corpus.csv','r') as csvfile:

import csv 
import sys
import random
import time

# Initialization

# Major Global Variables

# Number of network units to represent each phoneme
phon_length = 11

# Number of network units to represent human male/female concept
gender_length = 8

# Number of network units to represent Celtic substrate gender
slavic_length = 8

# Total number of possible phonemes for a word
stem_length = 30

# Number of network units at the output layer
out_length = 3

# Number of network units at the input layer
input_length = (stem_length * phon_length) + slavic_length + gender_length

# Gender dictionary for assigning input values
input_genders = {
	"m":(1,1,1,1,0,0,0,0),
	"f":(0,0,0,0,1,1,1,1),
	"n":(0,0,0,0,0,0,0,0)
}

# Gender dictionary for predicting outcome values
output_genders = {
	"m":(1,0,0),
	"f":(0,1,0),
	"n":(0,0,1)
}

# Adjust frequencies depending on case and human/nonhuman

human_case_freq = {
	"nomsg" : 8,
	"nompl" : 3,
	"accsg" : 4, #we'll implement the random addition at runtime
	"accpl" : 2, #we'll implement the random addition at runtime
	"gensg" : 4,
	"genpl" : 2,
}
nhuman_case_freq = {
	"nomsg" : 4,
	"nompl" : 2,
	"accsg" : 7, 
	"accpl" : 2, 
	"gensg" : 2,
	"genpl" : 1,
}

# The output dictionary should map (330) tuples to (3) tuples 

# corpus contains every word mapped to its latin gender
corpus = {}

# frequencies contains every word mapped to its frequency
frequencies = {}

# Dictonary/hashtable that maps phonemes to chomsky values
phonemes = {
	"p" : (-0.9, 0.9, -0.9, -0.9, -0.9, -0.9, 0.9, -0.9, 0.9, -0.9, 0.9), 
	"t" : (-0.9, 0.9, -0.9, -0.9, -0.9, -0.9, 0.9, -0.9, -0.9, -0.9, 0.9), 
	"k" : (-0.9, 0.9, -0.9, -0.9, -0.9, -0.9, -0.9, -0.9, 0.9, -0.9, 0.9), 
	"b" : (-0.9, 0.9, 0.9, -0.9, -0.9, -0.9, 0.9, -0.9, 0.9, -0.9, -0.9), 
	"d" : (-0.9, 0.9, 0.9, -0.9, -0.9, -0.9, 0.9, -0.9, -0.9, -0.9, -0.9), 
	"g" : (-0.9, 0.9, 0.9, -0.9, -0.9, -0.9, 0.9, -0.9, 0.9, -0.9, -0.9), 
	"f" : (-0.9, 0.9, -0.9, 0.9, 0.9, -0.9, 0.9, -0.9, 0.9, -0.9, 0.9), 
	"v" : (-0.9, 0.9, 0.9, 0.9, 0.9, -0.9, 0.9, -0.9, 0.9, -0.9, -0.9), 
	"s" : (-0.9, 0.9, -0.9, 0.9, 0.9, -0.9, 0.9, -0.9, -0.9, -0.9, 0.9),
    "z" : (-0.9, 0.9, 0.9, 0.9, 0.9, -0.9, 0.9, -0.9, -0.9, -0.9, -0.9),
	"h" : (-0.9, 0.9, -0.9, 0.9, -0.9, -0.9, -0.9, -0.9, 0.9, -0.9, 0.9), 
	"m" : (-0.9, 0.9, 0.9, -0.9, -0.9, 0.9, 0.9, -0.9, 0.9, -0.9, -0.9), 
	"n" : (-0.9, 0.9, 0.9, -0.9, -0.9, 0.9, 0.9, -0.9, -0.9,-0.9, -0.9), 
	"w" : (-0.9, -0.9, 0.9, 0.9, -0.9, -0.9, -0.9, -0.9, 0.9, 0.9, -0.9), 
	"r" : (-0.9, -0.9, 0.9, 0.9, -0.9, -0.9, 0.9, -0.9, -0.9, -0.9, -0.9), 
	"l" : (0.9, 0.9, 0.9, 0.9, -0.9, -0.9, 0.9, -0.9, -0.9, -0.9, -0.9), 
	"y" : (-0.9, -0.9, 0.9, 0.9, -0.9, -0.9, -0.9, -0.9, -0.9, -0.9, -0.9), 
	"i" : (0.9, -0.9, 0.9, 0.9, -0.9, -0.9, 0.9, -0.9, -0.9, -0.9, -0.9),	#(wick)
	"u" : (0.9, -0.9, 0.9, 0.9, -0.9, -0.9, 0.9, -0.9, 0.9, 0.9, 0.9),	#(woo)
	"e" : (0.9, -0.9, 0.9, 0.9, -0.9, -0.9, -0.9, -0.9, -0.9, -0.9, -0.9),#(wed)
	"o" : (0.9, -0.9, 0.9, 0.9, -0.9, -0.9, -0.9, 0.9, 0.9, 0.9, -0.9),	#(cot)
	"a" : (0.9, -0.9, 0.9, 0.9, -0.9, -0.9, -0.9, 0.9, 0.9, -0.9, 0.9),	#(card)
	"*" : (0.9, -0.9, 0.9, 0.9, -0.9, -0.9, 0.9, -0.9, 0.9, -0.9, -0.9),	#(about)
	"-" : (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
}

# turn a syllable into its phonemic representation
# takes a six tuple
def print_phons((a,b,c,d,e,f)):
	return(phonemes[a] + phonemes[b] + phonemes[c] + phonemes[d] + phonemes[e] + phonemes[f])	 

# takes a corpus file and returns a tuple of dictionaries and an array.
# the first dictionary maps the numerical representaiton of each word to the numerical representaiton of its expected gender
# the second dictionary maps that numerical representaiton of each word to its frequency for training the dataset.
def convert_to_input(FILE):
	reader = csv.reader(open(FILE,'rU'))

	# loop over all of the rows in the input file
	for row in reader:

		# if it's a new word
		if row[0] == "_": # some indication that this row marks the beginning of a new word
			# get the crucial information 
			# we expect gen to be the lower case gender
			[word, gen, pr, po, freq, slav] = row[1:]
					# what are pr and po? we use everything else

			#save the frequency
			orig_freq = freq

		# otherwise we know these values, and want to add a new word to the dictionary
		else:
			# reset the frequency
			freq = orig_freq

			# get the specifics of the word
			[s1, s2, s3, s4, s5, case, suf, dem, adj] = row

			# nonhuman referents (adjst frequency)
			if gen == "n":
				freq *= nhuman_case_freq[case]
			
			# human referents (adjust frequency)
			else:
				# make the random addition
				if case == "accsg" or "accpl":
					freq *= (human_case_freq[case] + random.randint(0,2))
				#othewise just the regular
				else:
					freq *= (human_case_freq[case])
			
			# convert all the phonemes into their numerical representaiton
			map(print_phons, [s1,s2,s3,s4,s5])

			#add them to the input
			input_tuple = s1+s2+s3+s4+s5

			# sanity check
			if len(input_tuple) != (stem_length * phon_length):
				print len(input_tuple), input_length
				raise SystemExit

			# add the two genders
			input_tuple += input_genders[gen] 
			input_tuple += input_genders[slav] 

			# sanity check
			if len(input_tuple) != input_length:
				print len(input_tuple), input_length
				raise SystemExit
			
			# now we have the input tuple for this word. We need to add it and its expected output to the dictionary
			
			# sanity check 
			if input_tuple in corpus.keys():
				print "what are you playing at"
				raise SystemExit

			# add it once to the corpus, paired with its latin gender
			currentLatinGender = output_genders[gen]
			corpus.update({input_tuple:currentLatinGender})

			# add it to frequencies with its frequency
			frequencies.update({input_tuple:freq})
	# create the training set
	training_corpus = []

	# loop over the words
	for x in corpus.keys():
		# add it as many times as its frequency
		for y in xrange(frequencies[x]):
			training_corpus.append((x,corpus[x]))
	
	# now randomize it
	random.shuffle(training_corpus)


	return(corpus, frequencies, training_corpus)




		