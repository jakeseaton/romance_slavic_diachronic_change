#
#
# Program to generate an ?SNNS? input file for Tyler Lau's project.
# Code based on Perl version written by Ezra Van Everbroeck in 2003.
# Developed in Python by Jake Seaton
#
#
# Modifications from original: less strict with the input and output files

import sys
import random
import time
# Initialization

# Major Global Variables

# Number of network units to represent each phoneme
Phon_length = 11

# Number of network units to represent human male/female concept
Gender_length = 8

# Number of network units to represent Celtic substrate gender
Celtic_length = 8

# Total number of possible phonemes for a word
Stem_length = 30

# Number of network units at the output layer
Output_length = 3

# Number of network units at the input layer
Input_length = (Stem_length * Phon_length) + Celtic_length + Gender_length

# #reset random seed
# random.seed()
# 	#this uses system time


# # get the time 
# time = time.localtime(time.time())


# Convert input to chomsky representation
#use a dictionary that maps keys to values.
phonemes = {
	"p" : "-0.9 0.9 -0.9 -0.9 -0.9 -0.9 0.9 -0.9 0.9 -0.9 0.9 ", 
	"t" : "-0.9 0.9 -0.9 -0.9 -0.9 -0.9 0.9 -0.9 -0.9 -0.9 0.9 ", 
	"k" : "-0.9 0.9 -0.9 -0.9 -0.9 -0.9 -0.9 -0.9 0.9 -0.9 0.9 ", 
	"b" : "-0.9 0.9 0.9 -0.9 -0.9 -0.9 0.9 -0.9 0.9 -0.9 -0.9 ", 
	"d" : "-0.9 0.9 0.9 -0.9 -0.9 -0.9 0.9 -0.9 -0.9 -0.9 -0.9 ", 
	"g" : "-0.9 0.9 0.9 -0.9 -0.9 -0.9 0.9 -0.9 0.9 -0.9 -0.9 ", 
	"f" : "-0.9 0.9 -0.9 0.9 0.9 -0.9 0.9 -0.9 0.9 -0.9 0.9 ", 
	"v" : "-0.9 0.9 0.9 0.9 0.9 -0.9 0.9 -0.9 0.9 -0.9 -0.9 ", 
	"s" : "-0.9 0.9 -0.9 0.9 0.9 -0.9 0.9 -0.9 -0.9 -0.9 0.9 ",
    "z" : "-0.9 0.9 0.9 0.9 0.9 -0.9 0.9 -0.9 -0.9 -0.9 -0.9 ",
	"h" : "-0.9 0.9 -0.9 0.9 -0.9 -0.9 -0.9 -0.9 0.9 -0.9 0.9 ", 
	"m" : "-0.9 0.9 0.9 -0.9 -0.9 0.9 0.9 -0.9 0.9 -0.9 -0.9 ", 
	"n" : "-0.9 0.9 0.9 -0.9 -0.9 0.9 0.9 -0.9 -0.9 -0.9 -0.9 ", 
	"w" : "-0.9 -0.9 0.9 0.9 -0.9 -0.9 -0.9 -0.9 0.9 0.9 -0.9 ", 
	"r" : "-0.9 -0.9 0.9 0.9 -0.9 -0.9 0.9 -0.9 -0.9 -0.9 -0.9 ", 
	"l" : "0.9 0.9 0.9 0.9 -0.9 -0.9 0.9 -0.9 -0.9 -0.9 -0.9 ", 
	"y" : "-0.9 -0.9 0.9 0.9 -0.9 -0.9 -0.9 -0.9 -0.9 -0.9 -0.9 ", 
	"i" : "0.9 -0.9 0.9 0.9 -0.9 -0.9 0.9 -0.9 -0.9 -0.9 -0.9 ",	#(wick)
	"u" : "0.9 -0.9 0.9 0.9 -0.9 -0.9 0.9 -0.9 0.9 0.9 0.9 ",	#(woo)
	"e" : "0.9 -0.9 0.9 0.9 -0.9 -0.9 -0.9 -0.9 -0.9 -0.9 -0.9 ",#(wed)
	"o" : "0.9 -0.9 0.9 0.9 -0.9 -0.9 -0.9 0.9 0.9 0.9 -0.9 ",	#(cot)
	"a" : "0.9 -0.9 0.9 0.9 -0.9 -0.9 -0.9 0.9 0.9 -0.9 0.9 ",	#(card)
	"*" : "0.9 -0.9 0.9 0.9 -0.9 -0.9 0.9 -0.9 0.9 -0.9 -0.9 ",	#(about)
	"-" : "0 0 0 0 0 0 0 0 0 0 0 "
}

# Get input file
#If specified on command line
if (sys.argv[1]):
	# use it
	infile = sys.argv[1]
# Otherwise ask for it
else: infile = raw_input("Filename with inputs? : ")

# Make sure we can read input file


# # Get output file
# if (sys.argv[2]):
# 	outfile = sys.argv[2]
# else: outfile = raw_input("Filename for .pat? : ")

# Make sure we can write to it

# reset record separator so we get everything for a word at once
record_separator = "\n_	"


#### Read input and write output
try:
	with open(infile, "r") as input_file:
         except IOError:
            print ("Cannot open file")
		sys.exit(1)
