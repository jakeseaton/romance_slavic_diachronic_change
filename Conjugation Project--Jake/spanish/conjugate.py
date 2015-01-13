# coding=Latin-1
import random
import verbs
print "-----Welcome to Verlbe Conjugate!-----"
print "Enter the correct conjuguation. When you reach 1000 points, you win!"

tenses = ["indicative", "preterite", "imperfect", "present participle", "past participle","future","conditional","present subjunctive", "imperfect subjunctive","affirmative command", "negative command"]

# initialize the score
score = 0
scale = 1
num_right = 0

# a complete array
complete = []

# main
while (True):
	#choose a random tense
	tense = random.choice(tenses)
	verb_type = random.choice(verbs.types)
	verb = random.choice(verb_type.keys())
	english = verb_type.get(verb)

	# if we haven't already seen these
	if (not((verb, tense) in complete)):
		passed = True
		# figure out the type of verb
		if verb_type == verbs.regular_ar:
			instance = verbs.ar(verb)
		elif verb_type == verbs.regular_er:
			instance = verbs.er(verb)
		elif verb_type == verbs.regular_ir:
			instance = verbs.ir(verb)
		else: #Verb is irregular
			raise SystemExit
	# do something about the present perfect tense
	if tense == "present perfect":
		# get the past participle
		print verb
		past_participle = instance.conjugate("past participle").values()[0]
		current_verb = dict(zip(verbs.pronouns, verbs.present_haber))
		for x in current_verb.keys():
			current_verb[x] = current_verb[x] + " " + past_participle
	else: # it doesn't need the auxillary 
		current_verb = instance.conjugate(tense)
	while current_verb:
		(pronoun, correct_answer) = current_verb.popitem()
		print pronoun, english, tense
		user_answer = raw_input()
		decoded = user_answer.decode('Latin-1')
		if correct_answer == decoded:
			num_right += 1
			score += 1 * (scale ** 2)
			if score >= 1000:
				print "You Win!"
				raise SystemExit
			scale += 1
			print "~~Correct! Score: %s. Complete: %s~~" % (score, num_right)
		else:
			print "The correct answer is:"
			print correct_answer.encode('Latin-1')
			scale = 1
			passed = False
			correction = raw_input()
			correction = raw_input("One More Time. ")
			while not(correction.decode('Latin-1') == correct_answer):
				print "Keep trying!"
				correction = raw_input()
	if passed:
		print "You have completed this verb"
		complete.append((verb, tense))