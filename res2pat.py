import math
import sys

semvector = [[1,0,0],[0,1,0],[0,0,1]]

# initialize array with a certain numer of indices
def make_array(indices, init):
	return [init for x in xrange(indices)]

# Create the char arrays with 90 slots
# [title, date, undef, pats, ins, outs] = [make_array(90,0) for x in xrange(6)]

# Create the char arrays with 120 slots
# [line, dit] = [make_array(120) for x in xrange(2)]

# Create the rest of the variables, though they can be implicitly defined

# Create the float array
raw = make_array(80,0.0)

# Call the input file f1

def main():
	# declare a string p
	# and three ints i,j,k

	# open the input file
	try: 
		with open(sys.argv[1], "r") as f1:
			title = f1.read(81)
			date = f1.read(81)
			undef = f1.read(81)
			pats = f1.read(81)
			ins = f1.read(81)
			outs = f1.read(81)
			undef = f1.read(81)
			undef = f1.read(81)
			undef = f1.read(81)
		 	
		 	print("SNNS pattern definition file V1.4\n")
		 	print("%s\n\n" % date)
		 	print("%s" % pats)
		 	print("%s" % ins)
		 	print("%s" % outs)
		 
		 	pat = findint(pats)
			In = findint(ins)
			out = findint(outs)

			for i in range(0,pat):
				# comment line
				line = f1.read(81)
				print("%s" % line)

				# input line 
				for j in range(0, In):
					# i know this is wrong
					dit = string(f1)
					print("%s", dit)
					# I'm confused about this code. It needs to mimmick:
					#fscanf(f1, "%s", dit);
					#printf("%s ", dit);

				# output line
				for k in range(0, out):
					# what does this ampersand mean?
					# this needs to mimmick
					#fscanf(f1, "%f", &raw[k]);
					raw[k] = float(f1)
					# i know this is wrong
				distf()
				print("\n")
				line = f1.read(10)
		except IOError:
			print ("Cannot open file")
			sys.exit(1)


# Compute the Euclidean calculation of error
def distf():
	bestdist = 100000.0
	bestpointer = 0
	for j in range(0,3):
		dist = 0.0
		for k in range(0,3):
			temp = semvector[j][k] - raw[k]
			dist += temp * temp
		if dist < bestdist:
			bestdist = dist;
			bestpointer = j;

	#print it out
	for k in range(0,3):
		print("%s ", % semvector[bestpointer][k])

# Get the  number which is in a char line
def findint(text): #text is a pointer to a character
	i = 0
	j = 0
	while text[i]:
		if (text[i].isdigit()):
			text[j] = text[i]
			j += 1
		i += 1
	text[j] = ""
	return(int(''.join(text))
