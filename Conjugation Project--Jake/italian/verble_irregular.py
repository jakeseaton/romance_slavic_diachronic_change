# TO DO 
# A seen array,
# have it make you conjugate every form of the verb. have the conjugate function return a dictionary of all the conjugations, and then pop one off 
import random
import iverbs


print "------Welcome to Verble Conjugate! (Irregular Edition)------"
print "Enter the correct conjugation. When you reach 1000 points, you win!"

# tenses
tenses = ["indicative"]

#verbs
verbs = iverbs.verbs

# initialize the score
score = 0
scale = 1
num_right = 0

# a complete array
complete = []

# main
while (True):
	# choose a random irregular verb in english
	verb = random.choice(verbs.keys())
	# choose a random tense
	tense = random.choice(tenses)
	if not((verb, tense) in complete):
		# get the dictionary of conjugations associated with it
		verb_dict = verbs.get(verb)
		# get the conjugated dictionary in that tense
		conjugated = iverbs.conjugate(verb_dict, tense)
		# passed
		passed = True
		# loop through it and ask every question
		while (conjugated):
			(pronoun, correct_answer) = conjugated.popitem()
			print pronoun + " " + verb + " "+ tense 
			user_answer = raw_input()
			if correct_answer == user_answer:
				num_right += 1
				score += 1 * (scale ** 2)
				if score >= 1000:
					print "You Win!"
					raise SystemExit
				scale += 1
				print "~~Correct! Score: %s. Complete: %s~~" % (score, num_right)
			else:
				passed = False
				print "The correct answer is:"
				print correct_answer
				scale = 1
				correction = raw_input()
				correction = raw_input("One more time. ")
				while not(correction == correct_answer):
					print "Keep trying!"
					correction = raw_input()
		if passed:
			complete.append((verb, tense))
			
