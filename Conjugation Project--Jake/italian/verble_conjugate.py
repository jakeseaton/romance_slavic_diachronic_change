# you can get the nanme of an object instance as a string with the function get_name
import random
import verbs
# print "something is wrong print out all of the types each time because go does not work"
print "------Welcome to Verble Conjugate!------"
print "Enter the correct conjugation. When you reach 1000 points, you win!"

# tenses
tenses = ["indicative", "imperfect"]
# "past participle"

# initialize the score
score = 0
scale = 1
num_right = 0

# a complete array
complete = []

# IMPLEMENT SEEN
# main
while (True):
	verb_type = random.choice(verbs.tipos)
	verb = random.choice(verb_type.keys())
	english = verb_type.get(verb)
	tense = random.choice(tenses)
	# if we haven't already seen these
	if (not((verb, tense) in complete)):
		passed = True
		# figure out the type of verb
		if verb_type == verbs.regulare_are:
			instance = verbs.are(verb)
		elif verb_type == verbs.regulare_ere:
			instance = verbs.ere(verb)
		elif verb_type == verbs.go_verbs:
			instance = verbs.go(verb)
		elif verb_type == verbs.gare_care:
			instance = verbs.gc_are(verb)
		elif verb_type == verbs.regulare_ire:
			instance = verbs.ire(verb)
		else:
			instance = verbs.isc(verb)
		current_verb = instance.conjugate(tense)
		while current_verb:
			(pronoun, correct_answer) = current_verb.popitem()
			print pronoun, english, tense
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
				print "La risposta corretta e:"
				print correct_answer
				scale = 1
				passed = False
				correction = raw_input()
				correction = raw_input("Un'altra volta. ")
				while not(correction == correct_answer):
					print "Keep trying!"
					correction = raw_input()
		if passed:
			print "Avete completato questo verbo"
			complete.append((verb, tense))
